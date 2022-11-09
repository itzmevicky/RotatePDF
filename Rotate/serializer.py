from rest_framework import serializers

class PDFRotateSerializer(serializers.Serializer):
    roatate = (
        ('90 Degree'),
        ('180 Degree'),
        ('270 Degree'),
        ('360 Degree'),
    )

    Upload_File = serializers.FileField(use_url=False)
    
    Rotation = serializers.ChoiceField(choices=roatate) 

    Page_Number_To_Rotate = serializers.IntegerField()


    class Meta:
        fields = ['Upload_File','Rotation','Page_Number_To_Rotate']




