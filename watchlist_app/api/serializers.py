from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Review


######## Model Serializers #################

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    
    # reviews below will be commented and will not be available till uncomment and made a new serate section for review
    reviews = ReviewSerializer(many=True, read_only=True)

    #overriding platform - so that instead of id in list-name should be visible not id.
    # platform = serializers.CharField(source='platform.name', read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    # Nested Serializer
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'

























############# Serializers ###################

# #using valiators
# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name is too short !!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])     
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #object level validation
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Both cant be same !!")
#         return data
    
    # field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short !!")
    #     return value    