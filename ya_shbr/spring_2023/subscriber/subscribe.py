import copy
import json


class Subscriber:
    def __init__(self, fields: list[str]):
        self.fields = fields

    def data_updated(self, trace_id: str, data: dict):
        printed_data = {
            "trace_id": trace_id, "offer": {"id": data["id"]}, }

        for field in self.fields:
            if field in data:
                printed_data["offer"][field] = data[field]

        print(json.dumps(printed_data, separators=(",", ":")))


class OfferRepository:
    def __init__(self):
        self.subscribers: list[(Subscriber, list[str])] = []
        self.storage: dict[str, dict] = {}

    def add_subscriber(self, subscriber: Subscriber, trigger_fields: list[str]):
        self.subscribers.append((subscriber, trigger_fields))

    def get_subscribers_for_notify(self, old_offer: dict, new_offer: dict) -> list:
        subscribers = []

        for (subscriber, trigger_fields) in self.subscribers:
            for field in trigger_fields:
                if field in new_offer and old_offer.get(field) != new_offer.get(field):
                    subscribers.append(subscriber)
                    break
        return subscribers

    def update(self, update_message: dict):
        update_offer = update_message["offer"]
        new_offer = copy.deepcopy(self.storage.setdefault(update_offer["id"], {}))
        for key in update_offer:
            if isinstance(new_offer.get(key), dict):
                new_offer[key].update(update_offer[key])
            else:
                new_offer[key] = update_offer[key]
        subscribers = self.get_subscribers_for_notify(
            self.storage[update_offer["id"]], new_offer
        )
        self.storage[update_offer["id"]] = new_offer
        self.notify_subscribers(subscribers, update_message["trace_id"], new_offer)

    @staticmethod
    def notify_subscribers(subscribers: list[Subscriber], trace_id: str, data: dict):
        for subscriber in subscribers:
            subscriber.data_updated(trace_id, data)


if __name__ == "__main__":
    repository = OfferRepository()
    n, m = map(int, input().split())
    for _ in range(n):
        subscriber_info = input().split()
        number_trigger_fields = int(subscriber_info[0])
        fields = subscriber_info[2:]
        repository.add_subscriber(Subscriber(fields), fields[:number_trigger_fields])

    for _ in range(m):
        repository.update(json.loads(input()))