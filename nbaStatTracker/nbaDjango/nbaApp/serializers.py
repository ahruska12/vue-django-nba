from rest_framework import serializers
from rest_framework_jwt.serializers import User

from .models import Team, Player, Comparison, FavoriteTeam, FavoritePlayer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_id',
                  'name',
                  'abbreviation',
                  'city',
                  'state',
                  'conference',
                  'division',
                  'wins',
                  'losses',
                  'team_ppg',
                  'team_rpg',
                  'team_apg',
                  'opp_ppg'
                  )


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(slug_field='name', queryset=Team.objects.all())

    class Meta:
        model = Player
        fields = ('player_id',
                  'name',
                  'team',
                  'points',
                  'rebounds',
                  'assists',
                  'steals',
                  'blocks',
                  'games_played'
                  )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={'input_type': 'password'},
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True,
                                      style={'input_type': 'password'},
                                      required=True)

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'password2',
                  'email',
                  'first_name',
                  'last_name')
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True},
                        'password': {'write_only': True, 'min_length': 6},
                        'password2': {'write_only': True, 'min_length': 6}
                        }

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})
            return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class FavoriteTeamSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()

    def get_team(self, obj):
        team = obj.team.first()
        return team.name if team else None

    class Meta:
        model = FavoriteTeam
        fields = ('team',)


class FavoritePlayerSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField()

    def get_player(self, obj):
        player = obj.player.first()
        return player.name if player else None

    class Meta:
        model = FavoritePlayer
        fields = ('player',)


class ComparisonSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = ('name', 'wins', 'losses', 'team_ppg', 'team_rpg', 'team_apg', 'opp_ppg')


class PlayerComparisonSerializer(serializers.Serializer):
    class Meta:
        model = Player
        fields = ('player_id',
                  'name',
                  'team',
                  'points',
                  'rebounds',
                  'assists',
                  'steals',
                  'blocks',
                  'games_played'
                  )
