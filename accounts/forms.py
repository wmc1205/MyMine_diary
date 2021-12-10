from django.contrib.auth.forms import UserCreationForm

#ID 변경이 되는 문제를 해결하기 위해, UserCreationForm 가공
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
