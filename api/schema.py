import strawberry
from  strawberry.fastapi import GraphQLRouter

from apps.houses.schema import schemas as ml_schema


class Mutation(ml_schema.HouseMutation):
    pass


class Query(ml_schema.Query):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")


