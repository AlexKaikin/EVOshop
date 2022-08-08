from rest_framework import serializers

from apps.core.models import Category, Product, Review, Tag


class FilterReviewListSerializer(serializers.ListSerializer):
    """ Фильтр отзывов, только parent """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ Вывод ответов на отзывы """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    """ Список категорий """
    class Meta:
        model = Category
        exclude = ('slug', 'published', 'id', 'created', 'updated')


class ReviewSerializer(serializers.ModelSerializer):
    """ Список отзывов """
    class Meta:
        model = Review
        exclude = ('published', 'id', 'created')

    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    profile = serializers.SlugRelatedField(slug_field='username', read_only=True)


class ReviewForProductSerializer(serializers.ModelSerializer):
    """ Список отзывов """
    class Meta:
        model = Review
        exclude = ('published', 'id', 'created')
        list_serializer_class = FilterReviewListSerializer

    children = RecursiveSerializer(many=True)
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    profile = serializers.SlugRelatedField(slug_field='username', read_only=True)


class ReviewCreateSerializer(serializers.ModelSerializer):
    """ Список отзывов """
    class Meta:
        model = Review
        fields = '__all__'

    profile = serializers.HiddenField(default=serializers.CurrentUserDefault())


class ProductSerializer(serializers.ModelSerializer):
    """ Список товаров """
    class Meta:
        model = Product
        exclude = ('slug', 'published', 'id', 'created', 'updated')

    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tag = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewForProductSerializer(many=True)


class ProductCreateSerializer(serializers.ModelSerializer):
    """ Список товаров """
    class Meta:
        model = Product
        exclude = ('slug', )


class TagSerializer(serializers.ModelSerializer):
    """ Список меток к товарам """
    class Meta:
        model = Tag
        exclude = ('slug', 'id',)
