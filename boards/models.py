from django.db import models

def doubleDigit(number) :
    if number < 10 :
        return '0' + str(number)
    else :
        return '' + str(number)


class Board(models.Model) :
    code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        "users.User", 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='boards'
    )
    loadedfile = models.FileField(blank=True, null=True)
    file_link = models.URLField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def datetime(self) :
        dateObj = self.created_at
        return f"{dateObj.year}-{doubleDigit(dateObj.month)}-{doubleDigit(dateObj.day)} {doubleDigit(dateObj.hour)}:{doubleDigit(dateObj.minute)}:{doubleDigit(dateObj.second)}"