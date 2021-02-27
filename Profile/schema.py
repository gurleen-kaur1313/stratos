from inspect import Arguments
from django.core.checks.messages import Info
import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import User,PeriodTracker,Exercise
from graphql import GraphQLError
from django.db.models import Q


class Users(DjangoObjectType):
    class Meta:
        model = User

class Period(DjangoObjectType):
    class Meta:
        model = PeriodTracker

class GetExercise(DjangoObjectType):
    class Meta:
        model = Exercise


class Query(graphene.ObjectType):
    allUsers = graphene.List(Users, id=graphene.String(required=True))
    me = graphene.Field(Users)
    getperiodinfo = graphene.List(Period)
    getexerciseinfo = graphene.List(GetExercise)

    def resolve_allUsers(self, info, id):
        return User.objects.get(id=id)

    def resolve_me(self, info):
        user = info.context.user
        return user

    def resolve_getperiodinfo(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return PeriodTracker.objects.filter(user=active).order_by("-added")

    def resolve_getexerciseinfo(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Exercise.objects.filter(user=active).order_by("-added")

        



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
        nuser.BMI = nuser.Weight/(nuser.Height*nuser.Height)
        nuser.save()

        return CreateUser(user=nuser)


class UpdateProfile(graphene.Mutation):
    profile = graphene.Field(Users)

    class Arguments:
        email = graphene.String()
        name = graphene.String()
        mobile = graphene.String()
        state = graphene.String()
        city = graphene.String()
        age = graphene.Int()
        height = graphene.Int()
        weight = graphene.Int()
        gender = graphene.String()

    def mutate(self, info, **kwargs):
        myProfile = info.context.user
        if myProfile.is_anonymous:
            raise GraphQLError("Not Logged In!")
        myProfile.name = kwargs.get("name")
        myProfile.mobile = kwargs.get("mobile")
        myProfile.state = kwargs.get("state")
        myProfile.city = kwargs.get("city")
        myProfile.Age = kwargs.get("age")
        myProfile.Height = kwargs.get("height")
        myProfile.Weight = kwargs.get("weight")
        A = kwargs.get("height")
        B = kwargs.get("weight")
        myProfile.Gender = kwargs.get("gender")
        myProfile.BMI = B/(A*A)
        myProfile.save()

        return UpdateProfile(profile=myProfile)

class AddPeriodinfo(graphene.Mutation):
    info = graphene.Field(Period)

    class Arguments:
        date = graphene.Int()
        month = graphene.Int()
        year = graphene.Int()


    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        period = PeriodTracker.objects.create(user=user)
        period.date = kwargs.get("date")
        period.month = kwargs.get("month")
        period.year = kwargs.get("year")

        period.save()

        return AddPeriodinfo(info=period)

class AddExercise(graphene.Mutation):
    info = graphene.Field(GetExercise)

    class Arguments:
        date = graphene.Int()
        month = graphene.Int()
        year = graphene.Int()
        exercise_type = graphene.String()


    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        exercise = Exercise.objects.create(user=user)
        exercise.date = kwargs.get("date")
        exercise.month = kwargs.get("month")
        exercise.year = kwargs.get("year")
        exercise.exercise_type = kwargs.get("exercise_type")

        exercise.save()

        return AddExercise(info=exercise)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_profile = UpdateProfile.Field()
