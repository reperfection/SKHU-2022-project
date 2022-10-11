from django.contrib import admin
from .models import IT, ITAnswer, ITQuestion
from .models import Humanity, HumanityAnswer, HumanityQuestion
from .models import MediaContent, MediaContentsAnswer, MediaContentsQuestion
from .models import Society, SocietyAnswer, SocietyQuestion

# Register your models here.
admin.site.register(IT)
admin.site.register(ITQuestion)
admin.site.register(ITAnswer)

admin.site.register(Humanity)
admin.site.register(HumanityAnswer)
admin.site.register(HumanityQuestion)

admin.site.register(Society)
admin.site.register(SocietyAnswer)
admin.site.register(SocietyQuestion)

admin.site.register(MediaContent)
admin.site.register(MediaContentsAnswer)
admin.site.register(MediaContentsQuestion)