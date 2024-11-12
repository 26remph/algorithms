import copy
import json


class Subscriber:
    def __init__(self, fields: list[str]):
        self.fields = fields

    def output(self, trace_id: str, data: dict):
        out = {"trace_id": trace_id, "offer": {"id": data["id"]}}

        for field in self.fields:
            if field in data:
                out["offer"][field] = data[field]

        print(json.dumps(out, separators=(",", ":")))


class OfferStore:
    def __init__(self):
        self.subscribers: list[(Subscriber, list[str])] = []
        self.storage: dict[str, dict] = {}

    def add_subscriber(self, sub: Subscriber, trigger_fields: list[str]):
        self.subscribers.append((sub, trigger_fields))

    def get_subscribers(self, old_: dict, new_: dict) -> list:
        subscribers = []

        for subscriber, trigger_fields in self.subscribers:
            for field in trigger_fields:
                if field in new_ and old_.get(field) != new_.get(field):
                    subscribers.append(subscriber)
                    break
        return subscribers

    def update(self, inp_data: dict):
        update_offer = inp_data["offer"]
        trace_id = inp_data["trace_id"]

        new_offer = copy.deepcopy(self.storage.setdefault(update_offer["id"], {}))
        for key in update_offer:
            if isinstance(new_offer.get(key), dict):
                new_offer[key].update(update_offer[key])
            else:
                new_offer[key] = update_offer[key]

        subscribers = self.get_subscribers(self.storage[update_offer["id"]], new_offer)
        self.storage[update_offer["id"]] = new_offer
        for sub in subscribers:
            sub.output(trace_id, new_offer)


if __name__ == "__main__":
    store = OfferStore()
    n, m = map(int, input().split())
    for _ in range(n):
        a, b, *fields = input().split()
        store.add_subscriber(Subscriber(fields), fields[: int(a)])

    for _ in range(m):
        json_data = json.loads(input())
        # offer_before = store.save_before_update(json_data['offer']['id'])
        store.update(json_data)
        # store.notify(json_data, offer_before)
