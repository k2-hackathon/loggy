from ..services.aggregates import AggregateService

def get_lodgings(user_id: int):
    service = AggregateService()
    response = service.get_lodgings_data(user_id)
    return response
