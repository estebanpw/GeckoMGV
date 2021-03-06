from django import forms
from .models import models
from django.contrib.auth import get_user_model
from scripts.models import *
from fileSystem.views import *

User = get_user_model()

class RegisterService(forms.ModelForm):
    class Meta:
        fields = ["name", "exeName", "path", "help", "form"]
        model = Script

class ExecuteService(forms.Form):
    class Meta:
        fields = ["name", "args"]

class drawMSAComp(forms.Form):
    seq1=forms.CharField(label='Sequence2', max_length=100)
    seq2=forms.CharField(label='Sequence1', max_length=100)


class kmersForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Filename", widget=forms.Select(attrs={'class':'selector','id': 'Filename'}))
    parameter2 = forms.CharField(label='K', max_length=1, widget=forms.TextInput(attrs={'id': 'K'}))
    parameter3 = forms.CharField(label='fullOut', max_length=1, widget=forms.NumberInput(attrs={'id': 'fullOut'}))


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(kmersForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="Filename", widget=forms.Select(attrs={'class':'selector','id': 'Filename'}))

class csb2csvForm(forms.Form):
    parameter1 = forms.ChoiceField(label="CSB file", widget=forms.Select(attrs={'class':'selector','id': 'CSBfile'}))
    parameter2 = forms.ChoiceField(label="Master file", widget=forms.Select(attrs={'class':'selector','id': 'Masterfile'}))


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(csb2csvForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="CSB file", widget=forms.Select(attrs={'class':'selector','id': 'CSBfile'}))
        self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="Master file", widget=forms.Select(attrs={'class':'selector','id': 'Masterfile'}))

class reverseComplementForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Fasta to reverse", widget=forms.Select(attrs={'class':'selector','id': 'fastaToReverse'}))
    parameter2 = forms.CharField(label="Output file", widget=forms.TextInput(attrs={'class':'file','id': 'outputFile'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(reverseComplementForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Fasta to reverse", widget=forms.Select(attrs={'class':'selector','id': 'fastaToReverse'}))
        #self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Output file", widget=forms.Select(attrs={'class':'selector','id': 'outputFile'}))

class extractOverlappedForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Master file", widget=forms.Select(attrs={'class':'selector','id': 'masterFile'}))
    parameter2 = forms.CharField(label="Not overlapped output file", widget=forms.TextInput(attrs={'class':'file','id': 'nonOverlapped'}))
    parameter3 = forms.CharField(label="Overlapped output file", widget=forms.TextInput(attrs={'class':'file','id': 'overlapped'}))
    parameter4 = forms.ChoiceField(label="Sequence x", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter5 = forms.ChoiceField(label="Sequence y", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(extractOverlappedForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Master file", widget=forms.Select(attrs={'class':'selector','id': 'masterFile'}))

        #self.fields['parameter3'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Not Overlapped output file", widget=forms.Select(attrs={'class':'selector','id': 'nonOverlapped'}))
        #self.fields['parameter6'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Overlapped output file", widget=forms.Select(attrs={'class':'selector','id': 'overlapped'}))

        self.fields['parameter4'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence x", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter5'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence y", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class connectFragsUpForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Original frags file", widget=forms.Select(attrs={'class':'selector','id': 'originalFrags'}))
    parameter2 = forms.CharField(label="Output file", widget=forms.TextInput(attrs={'class':'file','id': 'outputFile'}))
    parameter3 = forms.ChoiceField(label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter4 = forms.ChoiceField(label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(connectFragsUpForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Original frags file", widget=forms.Select(attrs={'class':'selector','id': 'originalFrags'}))

        #self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Output file", widget=forms.Select(attrs={'class':'selector','id': 'outputFile'}))

        self.fields['parameter3'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter4'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class GeckoCSB(forms.Form):
    parameter1 = forms.ChoiceField(label="Original frags file", widget=forms.Select(attrs={'class':'selector','id': 'originalFrags'}))
    parameter2 = forms.CharField(label="Overlapped file", widget=forms.TextInput(attrs={'class':'file','id': 'overFile'}))
    parameter5 = forms.CharField(label="CSB file", widget=forms.TextInput(attrs={'class':'file','id': 'csbFile'}))
    parameter6 = forms.CharField(label="Master file", widget=forms.TextInput(attrs={'class':'file','id': 'masterFile'}))
    parameter3 = forms.CharField(label="iGap", widget=forms.TextInput(attrs={'id': 'igap'}))
    parameter4 = forms.IntegerField(label='eGap', widget=forms.TextInput(attrs={'id': 'egap'}))
    parameter7 = forms.ChoiceField(label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter8 = forms.ChoiceField(label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(GeckoCSB, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Original frags file", widget=forms.Select(attrs={'class':'selector','id': 'originalFrags'}))
        self.fields['parameter7'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter8'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class refineOverlappedForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Overlapped frags file", widget=forms.Select(attrs={'class':'selector','id': 'overFile'}))
    parameter2 = forms.ChoiceField(label="Not overlapped file", widget=forms.Select(attrs={'class':'selector','id': 'notFrags'}))
    parameter3 = forms.CharField(label="New Master frags file", widget=forms.TextInput(attrs={'class':'file','id': 'newMFile'}))
    parameter4 = forms.CharField(label="New overlapped frags file", widget=forms.TextInput(attrs={'class':'file','id': 'newOFrags'}))
    parameter5 = forms.CharField(label="New not overlapped frags file", widget=forms.TextInput(attrs={'class':'file','id': 'newNFile'}))
    parameter6 = forms.ChoiceField(label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter7 = forms.ChoiceField(label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(refineOverlappedForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Overlapped frags file", widget=forms.Select(attrs={'class':'selector','id': 'overFile'}))
        self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Not overlapped file", widget=forms.Select(attrs={'class':'selector','id': 'notFrags'}))
        #self.fields['parameter4'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="New Master frags file", widget=forms.Select(attrs={'class':'selector','id': 'newMFile'}))
        #self.fields['parameter5'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="New overlapped frags file", widget=forms.Select(attrs={'class':'selector','id': 'newOFrags'}))
        #self.fields['parameter6'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="New not overlapped frags file", widget=forms.Select(attrs={'class':'selector','id': 'newNFile'}))
        self.fields['parameter6'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter7'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class joinCSBwithOverlappedForm(forms.Form):
    parameter1 = forms.ChoiceField(label="CSB file", widget=forms.Select(attrs={'class':'selector','id': 'csbin'}))
    parameter2 = forms.ChoiceField(label="Overlapped file", widget=forms.Select(attrs={'class':'selector','id': 'overin'}))
    parameter3 = forms.CharField(label="CSB output", widget=forms.TextInput(attrs={'class':'file','id': 'csbout'}))
    parameter4 = forms.CharField(label="New master file", widget=forms.TextInput(attrs={'class':'file','id': 'newMaster'}))
    parameter5 = forms.CharField(label="iGap", widget=forms.TextInput(attrs={'id': 'igap'}))
    parameter6 = forms.IntegerField(label='eGap', widget=forms.TextInput(attrs={'id': 'egap'}))
    parameter7 = forms.ChoiceField(label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter8 = forms.ChoiceField(label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(joinCSBwithOverlappedForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="CSB file", widget=forms.Select(attrs={'class':'selector','id': 'csbin'}))
        self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Overlapped file", widget=forms.Select(attrs={'class':'selector','id': 'overin'}))
        self.fields['parameter7'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter8'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class classifyRepeatsForm(forms.Form):
    parameter4 = forms.CharField(label="Tandem repeats", widget=forms.TextInput(attrs={'class':'file','id': 'tandemFrags'}))
    parameter1 = forms.ChoiceField(label="Overlapped frags file", widget=forms.Select(attrs={'class':'selector','id': 'overFile'}))
    parameter2 = forms.ChoiceField(label="Not overlapped file", widget=forms.Select(attrs={'class':'selector','id': 'notFrags'}))
    parameter3 = forms.CharField(label="New Master frags file", widget=forms.TextInput(attrs={'class':'file','id': 'newMFile'}))
    parameter5 = forms.CharField(label="Interspersed repeats", widget=forms.TextInput(attrs={'class':'file','id': 'interFrags'}))
    parameter6 = forms.CharField(label="Duplications", widget=forms.TextInput(attrs={'class':'file','id': 'dupFile'}))
    parameter7 = forms.CharField(label="Not overlapped repeats", widget=forms.TextInput(attrs={'class':'file','id': 'notFile'}))
    parameter8 = forms.ChoiceField(label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter9 = forms.ChoiceField(label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(classifyRepeatsForm, self).__init__(*args, **kwargs)

        #self.fields['parameter4'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Tandem repeats", widget=forms.Select(attrs={'class':'selector','id': 'tandemFrags'}))
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Overlapped frags file", widget=forms.Select(attrs={'class':'selector','id': 'overFile'}))
        self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Not overlapped file", widget=forms.Select(attrs={'class':'selector','id': 'notFrags'}))
        #self.fields['parameter3'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="New Master frags file", widget=forms.Select(attrs={'class':'selector','id': 'newMFile'}))
        #self.fields['parameter5'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Interspersed repeats", widget=forms.Select(attrs={'class':'selector','id': 'interFrags'}))
        #self.fields['parameter6'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Duplications", widget=forms.Select(attrs={'class':'selector','id': 'dupFile'}))
        #self.fields['parameter7'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Nor overlapped repeats", widget=forms.Select(attrs={'class':'selector','id': 'notFile'}))
        self.fields['parameter8'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter9'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class geckoForm(forms.Form):
    choice=(("2","8"),("3","12"),("4","16"),("5","20"),("6","24"),("7","28"),("8","32"))
    parameter1 = forms.ChoiceField(label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
    parameter2 = forms.ChoiceField(label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))
    parameter3 = forms.IntegerField(label='Min length', widget=forms.TextInput(attrs={'id': 'leng'}))
    parameter4 = forms.CharField(label='Min similarity', max_length=3, widget=forms.TextInput(attrs={'id': 'sim'}))
    parameter5 = forms.ChoiceField(label='Word length', choices=choice, widget=forms.Select(attrs={'class':'selector','id': 'Wleng'}))
    parameter6 = forms.CharField(label='Fixed length', initial="1",widget = forms.HiddenInput())
    parameter7 = forms.CharField(label="Result csv", widget=forms.TextInput(attrs={'class':'file','id': 'csvout'}))
    parameter8 = forms.CharField(label="Result matrix", widget=forms.TextInput(attrs={'class':'file','id': 'matout'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(geckoForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence X FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqx'}))
        self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Sequence Y FASTA", widget=forms.Select(attrs={'class':'selector','id': 'seqy'}))

class muscleForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Multifasta file", widget=forms.Select(attrs={'class':'selector','id': 'input'}))
    parameter2 = forms.CharField(label="Multiple Alignment Output", widget=forms.TextInput(attrs={'class':'file','id': 'output'}))
    parameter3 = forms.CharField(label="Dendrogram Output", widget=forms.TextInput(attrs={'class':'file','id': 'output_dnd'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(muscleForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="Multifasta file", widget=forms.Select(attrs={'class':'selector','id': 'input'}))

class repKillerForm(forms.Form):
    parameter1 = forms.ChoiceField(label="CSV frags file", widget=forms.Select(attrs={'class':'selector','id': 'fragsFile'}))
    parameter2 = forms.CharField(label="Output Marked CSV", widget=forms.TextInput(attrs={'class':'file','id': 'outputFile'}))
    parameter3 = forms.IntegerField(label="Similarity Length", widget=forms.TextInput(attrs={'id':'SIM_POS'}))
    parameter4 = forms.IntegerField(label="Similarity Position", widget=forms.TextInput(attrs={'id':'SIM_LEN'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(repKillerForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="CSV frags file", widget=forms.Select(attrs={'class':'selector','id': 'fragsFile'}))

class CSVToPNGForm(forms.Form):
    parameter1 = forms.ChoiceField(label="CSV frags file", widget=forms.Select(attrs={'class':'selector','id': 'input'}))
    parameter2 =forms.CharField(label="Output filename", widget=forms.TextInput(attrs={'class':'file','id': 'output'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(CSVToPNGForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="CSV file", widget=forms.Select(attrs={'class':'selector','id': 'input'}))


### Internal Services Form - DONT USE class=file FOR OUTPUTE --> USE SIMPLE TEXT INSTEAD

class extractRepetitionsForm(forms.Form):
    choice=(("0","All"),("1", "Specific"))
    parameter1 = forms.ChoiceField(label="CSV file", widget=forms.Select(attrs={'class':'selector','id':'CSVfile'}))
    parameter2 = forms.ChoiceField(label="Extract Synteny Blocks", choices=choice, widget=forms.Select(attrs={'class':'selector','id':'boolSB'}))
    parameter3 = forms.IntegerField(label="Synteny Block ID (Optional)", required=False, widget=forms.TextInput(attrs={'id':'SID'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(extractRepetitionsForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="CSV file", widget=forms.Select(attrs={'class':'selector','id':'CSVfile'}))

class extractSequenceFromCSVForm(forms.Form):
    parameter1 = forms.ChoiceField(label="CSV frags file", widget=forms.Select(attrs={'class':'selector','id': 'fragsFile'}))
    parameter2 = forms.ChoiceField(label="X Fasta file", widget=forms.Select(attrs={'class':'selector','id': 'xFastaFile'}))
    parameter3 = forms.ChoiceField(label="Y Fasta file", widget=forms.Select(attrs={'class':'selector','id': 'yFastaFile'}))
    parameter4 = forms.ChoiceField(label="Y-Reversed Fasta file", widget=forms.Select(attrs={'class':'selector','id': 'yReversedFastaFile'}))
    parameter5 = forms.CharField(label="Output FastaFile", widget=forms.TextInput(attrs={'id': 'outputFastaFile'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(extractSequenceFromCSVForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="CSV frags file", widget=forms.Select(attrs={'class':'selector','id': 'fragsFile'}))
        self.fields['parameter2'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="X Fasta file", widget=forms.Select(attrs={'class':'selector','id': 'xFastaFile'}))
        self.fields['parameter3'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Y Fasta file", widget=forms.Select(attrs={'class':'selector','id': 'yFastaFile'}))
        self.fields['parameter4'] = forms.ChoiceField(choices=[(file.file.name, file.filename) for file in userFile.objects.filter(user=self.user)], label="Y-Reversed Fasta file", widget=forms.Select(attrs={'class':'selector','id': 'yReversedFastaFile'}))

class filterFragsForm(forms.Form):
    parameter1 = forms.ChoiceField(label="CSV frags file", widget=forms.Select(attrs={'class':'selector','id': 'input'}))
    parameter2 =forms.CharField(label="Output filename", widget=forms.TextInput(attrs={'id': 'output'}))
    parameter3 = forms.IntegerField(label='Identity', widget=forms.TextInput(attrs={'id': 'filterIdentity', 'type': 'number'}))
    parameter4 = forms.IntegerField(label='Min Lenght', widget=forms.TextInput(attrs={'id': 'filterLength', 'type': 'number'}))
    parameter5 = forms.IntegerField(label='Min Similarity', widget=forms.TextInput(attrs={'id': 'filterSimilarity', 'type': 'number'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(filterFragsForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="Multifasta file", widget=forms.Select(attrs={'class':'selector','id': 'input'}))


### Third Party Services Form

class clustalForm(forms.Form):
    parameter1 = forms.ChoiceField(label="Multifasta file", widget=forms.Select(attrs={'class':'selector','id': 'multifile'}))
    parameter2 =forms.CharField(label="Multiple Alignment Output", widget=forms.TextInput(attrs={'class':'file','id': 'output'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(clustalForm, self).__init__(*args, **kwargs)
        self.fields['parameter1'] = forms.ChoiceField(choices=[(file.file.name, file.filename)  for file in userFile.objects.filter(user=self.user)], label="Multifasta file", widget=forms.Select(attrs={'class':'selector','id': 'multifile'}))
