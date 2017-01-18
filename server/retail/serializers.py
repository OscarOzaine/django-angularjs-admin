from rest_framework import serializers
#from retail.models import Chain, Store, Employee
from django.contrib.auth.models import User
from rest_framework import serializers
from retail.models import Snippet
#, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class RangeParameterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    gpio = serializers.CharField(required=False, allow_blank=True, max_length=255)
    max = serializers.FloatField(required=False)
    max_value = serializers.FloatField(required=False)
    min = serializers.FloatField(required=False)
    min_value = serializers.FloatField(required=False)
    range_id = serializers.IntegerField(required=False)
    sensor_id = serializers.IntegerField(required=False)
    
    owner = serializers.ReadOnlyField(source='owner.username')
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        #lexer = get_lexer_by_name(self.language)
        #linenos = self.linenos and 'table' or False
        #options = self.title and {'title': self.title} or {}
        #formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        #self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.gpio = validated_data.get('gpio', instance.gpio)
        instance.max = validated_data.get('max', instance.max)
        instance.max_value = validated_data.get('max_value', instance.max_value)
        instance.min = validated_data.get('min', instance.min)
        instance.min_value = validated_data.get('min_value', instance.min_value)
        instance.range_id = validated_data.get('range_id', instance.range_id)
        instance.sensor_id = validated_data.get('sensor_id', instance.sensor_id)
        instance.save()
        return instance


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    #def save(self, *args, **kwargs):
    #    """
    #    Use the `pygments` library to create a highlighted HTML
    #    representation of the code snippet.
    #    """
    #    title = self.validated_data['title']
    #    code = self.validated_data['code']
    #    lineos = self.validated_data['lineos']
    #    owner = self.validated_data['owner']
        #queryset = Snippet.objects.all()
        #data = {'code': self.code}
        #serializer = SnippetSerializer(queryset=queryset, data=data)
        #lexer = get_lexer_by_name(self.language)
        #linenos = self.linenos and 'table' or False
        #options = self.title and {'title': self.title} or {}
        #formatter = HtmlFormatter(style=self.style, linenos=linenos,
        #                          full=True, **options)
        #self.highlighted = highlight(self.code, lexer, formatter)
        #serializer.is_valid()
        #serializer.save()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

# class ChainSerializer(serializers.ModelSerializer):
#     """ Serializer to represent the Chain model """
#     class Meta:
#         model = Chain
#         fields = ("name", "description", "slogan", "founded_date", "website")


# class StoreSerializer(serializers.ModelSerializer):
#     """ Serializer to represent the Store model """
#     class Meta:
#         model = Store
#         fields = (
#             "chain", "number", "address", "opening_date",
#             "business_hours_start", "business_hours_end"
#         )


# class EmployeeSerializer(serializers.ModelSerializer):
#     """ Serializer to represent the Employee model """
#     class Meta:
#         model = Employee
#         fields = ("store", "number", "first_name", "last_name", "hired_date")

