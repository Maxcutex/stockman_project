from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=100)
    exchange_code = models.CharField(max_length=50)
    sync_flag = models.CharField(max_length=30)
    logo = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class StructureType(models.Model):
    structure_type_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(max_length=100)
    structure_types = models.ManyToManyField(
        'self', through='StructureTypeRelationship', symmetrical=False)

    def __str__(self):
        return self.structure_type_name


class StructureTypeRelationship(models.Model):
    types = models.ManyToManyField('RelationshipType', blank=True,
                                   related_name='structure_type_relationships')
    from_structure_type = models.ForeignKey(
        'Structure', related_name='from_structure_types')
    to_structure_type = models.ForeignKey(
        'Structure', related_name='to_structure_types')

    class Meta:
        unique_together = ('from_structure_type', 'to_structure_type')


class Structure(models.Model):
    structure_name = models.CharField(max_length=100)
    structure_code = models.CharField(max_length=50)
    parent_id = models.CharField(max_length=100)
    structure_type = models.ForeignKey(StructureType, on_delete=models.CASCADE)
    structures = models.ManyToManyField(
        'self', through='StructureRelationship', symmetrical=False)
    is_active = models.BooleanField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.structure_name


class StructureRelationship(models.Model):
    types = models.ManyToManyField('RelationshipType', blank=True,
                                   related_name='structure_relationships')
    from_structure = models.ForeignKey(
        'Structure', related_name='from_structures')
    to_structure = models.ForeignKey('Structure', related_name='to_structures')

    class Meta:
        unique_together = ('from_structure', 'to_structure')
