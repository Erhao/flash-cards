from odmantic import Model
from bson import ObjectId


class Store(Model):
    name: str
    merchant_id: ObjectId
    address: str
