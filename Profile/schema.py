from inspect import Arguments
from django.core.checks.messages import Info
import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import User
from graphql import GraphQLError
from django.db.models import Q


class Users(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    allUsers = graphene.List(Users, id=graphene.String(required=True))
    me = graphene.Field(Users)

    def resolve_allUsers(self, info, id):
        return User.objects.get(id=id)

    def resolve_me(self, info):
        user = info.context.user
        return user



class CreateUser(graphene.Mutation):
    user = graphene.Field(Users)

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        name = graphene.String()
        mobile = graphene.String()
        state = graphene.String()
        city = graphene.String()
        age = graphene.Int()
        height = graphene.Int()
        weight = graphene.Int()
        gender = graphene.String()

    def mutate(self, info, **kwargs):
        nuser = User(email=kwargs.get("email"))
        nuser.set_password(kwargs.get("password"))
        nuser.name = kwargs.get("name")
        nuser.mobile = kwargs.get("mobile")
        nuser.state = kwargs.get("state")
        nuser.city = kwargs.get("city")
        nuser.Age = kwargs.get("age")
        nuser.Height = kwargs.get("height")
        nuser.Weight = kwargs.get("weight")
        nuser.Gender = kwargs.get("gender")
        nuser.save()

        return CreateUser(user=nuser)


class UpdateProfile(graphene.Mutation):
    profile = graphene.Field(Users)

    class Arguments:
        name = graphene.String()
        mobile = graphene.String()
        state = graphene.String()
        city = graphene.String()
        age = graphene.Int()
        height = graphene.Int()
        weight = graphene.Int()
        gender = graphene.String()

    def mutate(self, info, **kwargs):
        myProfile = User.objects.get(id=id)
        if myProfile.is_anonymous:
            raise GraphQLError("Not Logged In!")
        myProfile.name = kwargs.get("name")
        myProfile.mobile = kwargs.get("mobile")
        myProfile.state = kwargs.get("state")
        myProfile.city = kwargs.get("city")
        myProfile.Age = kwargs.get("age")
        myProfile.Height = kwargs.get("height")
        myProfile.Weight = kwargs.get("weight")
        myProfile.Gender = kwargs.get("gender")
        myProfile.save()

        return UpdateProfile(profile=myProfile)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_profile = UpdateProfile.Field()
