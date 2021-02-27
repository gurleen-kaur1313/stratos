import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import HealthEmergency
from graphql import GraphQLError
from django.db.models import Q

class Health(DjangoObjectType):
    class Meta:
        model = HealthEmergency

class Query(graphene.ObjectType):
    health = graphene.List(Health)

    def resolve_health(self,info):
        return HealthEmergency.objects.all().order_by("-time")


class AddHealthEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Health)

    class Arguments:
        locality = graphene.String()
        city = graphene.String()
        state = graohene.String()
        date = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        test = HealthEmergency.objects.create(user=user)
        test.locality = kwargs.get("locality")
        test.city = kwargs.get("city")
        test.state = kwargs.get("state")
        test.date = kwargs.get("date")
        test.save()
        return AddHealthEmergency(myEmergency=test)


class Mutation(graphene.ObjectType):
    add_emergency = AddHealthEmergency.Field()