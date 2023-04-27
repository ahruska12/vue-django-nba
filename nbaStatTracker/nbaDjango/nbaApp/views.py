from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from nbaApp.models import Team
from nbaApp.serializers import ComparisonSerializer



@csrf_exempt
@api_view(['GET', 'POST'])
def team_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getTeam(request, pk):
    """ Retrieve, update or delete a customer instance. """
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(team, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def player_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        player = Player.objects.all()
        serializer = PlayerSerializer(player, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getPlayer(request, pk):
    """ Retrieve, update or delete a customer instance. """
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PlayerSerializer(player, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlayerSerializer(player, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def compare_teams(request,team1_id,team2_id):
    permission_classes = (IsAuthenticatedOrReadOnly)

    try:
        team1 = Team.objects.get(team_id=team1_id)
        team2 = Team.objects.get(team_id=team2_id)

    except Team.DoesNotExist:
        return Response({'error': 'One or both teams not found'}, status=404)
    
    comparisons = [
            {
                'category': 'Wins',
                'team1_value': team1.wins,
                'team2_value': team2.wins,
            },
            {
                'category': 'Losses',
                'team1_value': team1.losses,
                'team2_value': team2.losses,
            },
            {
                'category': 'PPG',
                'team1_value': team1.team_ppg,
                'team2_value': team2.team_ppg,
            },
            {
                'category': 'RPG',
                'team1_value': team1.team_rpg,
                'team2_value': team2.team_rpg,
            },
            {
                'category': 'APG',
                'team1_value': team1.team_apg,
                'team2_value': team2.team_apg,
            },
            {
                'category': 'OPP PPG',
                'team1_value': team1.opp_ppg,
                'team2_value': team2.opp_ppg,
            }
        ]

    comparison_results = {}
    for comparison in comparisons:
            try:
    
                difference = int(comparison['team1_value']) - int(comparison['team2_value'])
            except ValueError:  
                difference = round(float(comparison['team1_value']) - float(comparison['team2_value']), 3)

            if difference > 0:
                comparison_results[comparison['category']] = {
                    'team1_name': team1.name,
                    'team1_value': comparison['team1_value'],
                    'team2_name': team2.name,
                    'team2_value': comparison['team2_value'],
                    'result': f"{team1.name} has more {abs(difference)} {comparison['category']}"
                }
            elif difference < 0:
                comparison_results[comparison['category']] = {
                    'team1_name': team1.name,
                    'team1_value': comparison['team1_value'],
                    'team2_name': team2.name,
                    'team2_value': comparison['team2_value'],
                    'result': f"{team1.name} has less {abs(difference)} {comparison['category']}"
                }
            else:
                comparison_results[comparison['category']] = {
                    'team1_name': team1.name,
                    'team1_value': comparison['team1_value'],
                    'team2_name': team2.name,
                    'team2_value': comparison['team2_value'],
                    'result': f"{team1.name} and {team2.name} both have the same {comparison['category']}"
                }

    return Response({"data":{
            'team1_name': team1.name,
            'team2_name': team2.name,
            'comparisons': comparison_results
        }})


@api_view(['GET'])
def compare_players(request, player1_id,  player2_id):
    permission_classes = (IsAuthenticatedOrReadOnly)

    if not player1_id or not player2_id:
        return Response({'error': 'Please provide both player1_id and player2_id'})
    try:
        player1 = Player.objects.get(player_id=player1_id)
        player2 = Player.objects.get(player_id=player2_id)
    except Player.DoesNotExist:
        return Response({'error': 'One or both player IDs are invalid'})
    
    comparisons = [
            {
                'category': 'Points',
                'player1_value': player1.points,
                'player2_value': player2.points,
            },
            {
                'category': 'Rebounds',
                'player1_value': player1.rebounds,
                'player2_value': player2.rebounds,
            },
            {
                'category': 'Assists',
                'player1_value': player1.assists,
                'player2_value': player2.assists,
            },
            {
                'category': 'Steals',
                'player1_value': player1.steals,
                'player2_value': player2.steals,
            },
            {
                'category': 'Blocks',
                'player1_value': player1.blocks,
                'player2_value': player2.blocks,
            },
            {
                'category': 'Games Played',
                'player1_value': player1.games_played,
                'player2_value': player2.games_played,
            }
        ]

    comparison_results = {}
    for comparison in comparisons:
        try:
    
            difference = int(comparison['player1_value']) - int(comparison['player2_value'])
        except ValueError:  
            difference = round(float(comparison['player1_value']) - float(comparison['player2_value']), 3)
        print(comparison['player1_value'],'and', comparison['player2_value'],'==',difference)
        if difference > 0:

            comparison_results[comparison['category']] = {
                    'player1_name': player1.name,
                    'player1_value': comparison['player1_value'],
                    'player2_name': player2.name,
                    'player2_value': comparison['player2_value'],
                    'result': f"{player1.name} has more {abs(difference)} {comparison['category']}"
                   
                }
        elif difference < 0:
            comparison_results[comparison['category']] = {
                    'player1_name': player1.name,
                    'player1_value': comparison['player1_value'],
                    'player2_name': player2.name,
                    'player2_value': comparison['player2_value'],
                    'result': f"{player1.name} has less {abs(difference)} {comparison['category']}"
                }
        else:
            comparison_results[comparison['category']] = {
                    'player1_name': player1.name,
                    'player1_value': comparison['player1_value'],
                    'player2_name': player2.name,
                    'player2_value': comparison['player2_value'],
                    'result': f"{player1.name} and {player2.name} both have the same {comparison['category']}"
                }

    return Response({'data':{
            'player1_name': player1.name,
            'player2_name': player2.name,
            'comparisons': comparison_results
        }})
            
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer