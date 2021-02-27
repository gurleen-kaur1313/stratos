import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import HealthEmergency,HealthTest
from graphql import GraphQLError
from django.db.models import Q

class Health(DjangoObjectType):
    class Meta:
        model = HealthEmergency

class TestForHealth(DjangoObjectType):
    class Meta:
        model = HealthTest

class Query(graphene.ObjectType):
    health = graphene.List(Health)
    getAllTest = graphene.List(TestForHealth)
    getMyTest = graphene.List(TestForHealth)

    def resolve_health(self,info):
        return HealthEmergency.objects.all().order_by("-time")

    def resolve_getAllTest(self, info):
        return HealthTest.objects.all()

    def resolve_getMyTest(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return HealthTest.objects.filter(user=active).order_by("-date")



class AddHealthEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Health)

    class Arguments:
        locality = graphene.String()
        city = graphene.String()
        state = graphene.String()
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

class AddHealthTest(graphene.Mutation):
    myTest = graphene.Field(TestForHealth)

    class Arguments:
        test = graphene.String()
        remarksDoc = graphene.String()
        remarksPat = graphene.String()

    def mutate(self, info, **kwargs):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        test = HealthTest.objects.create(user=active)
        test.test = kwargs.get("test")
        test.remarksDoc = kwargs.get("remarksDoc")
        test.remarksPat = kwargs.get("remarksPat")
        test.save()
        return AddHealthTest(myTest=test)


class Mutation(graphene.ObjectType):
    add_emergency = AddHealthEmergency.Field()
    add_test = AddHealthTest.Field()