# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Func

class Left(Func):
    function = 'LEFT'
    template = '%(function)s(%(expressions)s, 256)'

def get_truncated_value(model_class, field_name, instance):
    truncated_field = f"{field_name}_short"
    return model_class.objects.annotate(
        **{truncated_field: Left(field_name)}
    ).get(pk=instance.pk).__dict__[truncated_field]

# Example:
# general_instance = General.objects.get(pk=1)
# truncated_value = get_truncated_value(General, 'fldValue', general_instance)
# print(truncated_value)


class ApiChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('ApiQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_choice'


class ApiQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_question'


class Airline(models.Model):
    fldID           = models.AutoField(db_column='fldID', primary_key=True)
    fldStatus       = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldCode         = models.CharField(db_column='fldCode', max_length=20, default='')
    fldEnglishName  = models.CharField(db_column='fldEnglishName', max_length=200, default='')
    fldChineseName  = models.CharField(db_column='fldChineseName', max_length=200, default='')
    fldPicture      = models.TextField(db_column='fldPicture', blank=True, null=True)
    fldLastMDate    = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM     = models.CharField(db_column='fldEmpNameM', max_length=250, default='')
    fldWithDesks    = models.CharField(db_column='fldWithDesks', max_length=10, default='')
    fldHotline      = models.CharField(db_column='fldHotline', max_length=50, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldCode', 'fldStatus'], name='airline_fldNo'),
        ]
        db_table = 'tblairline'
        ordering = ['fldID']

    def __str__(self):
        return f"Name: {self.fldEnglishName} ({self.fldChineseName}), Code: {self.fldCode}, Status: {self.fldStatus}, Any Tranfer Desk: {self.fldWithDesks}, Hotline: {self.fldHotline}"
    
    @property
    def fldPicture_short(self):
        # return Airline.objects.annotate(fldPicture_short=Left('fldPicture')).get(pk=self.pk).fldPicture_short
        return get_truncated_value(Airline, 'fldPicture', self)

class AirlineBackup(models.Model):
    fldID           = models.AutoField(db_column='fldID', primary_key=True)
    fldStatus       = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldCode         = models.CharField(db_column='fldCode', max_length=20, default='')
    fldEnglishName  = models.CharField(db_column='fldEnglishName', max_length=200, default='')
    fldChineseName  = models.CharField(db_column='fldChineseName', max_length=200, default='')
    fldPicture      = models.TextField(db_column='fldPicture', blank=True, null=True)
    fldLastMDate    = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM     = models.CharField(db_column='fldEmpNameM', max_length=250, default='')
    fldWithDesks    = models.CharField(db_column='fldWithDesks', max_length=10, default='')
    fldHotline      = models.CharField(db_column='fldHotline', max_length=50, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldCode', 'fldStatus'], name='airlinebackup_fldNo'),
        ]
        db_table = 'tblairline_backup'
        ordering = ['fldID']

    def __str__(self):
        return f"Name: {self.fldEnglishName} ({self.fldChineseName}), Code: {self.fldCode}, Status: {self.fldStatus}, Any Tranfer Desk: {self.fldWithDesks}, Hotline: {self.fldHotline}"


class AirlineOpenTime(models.Model):
    fldID           = models.AutoField(db_column='fldID', primary_key=True)
    fldAirlineID    = models.IntegerField(db_column='fldAirlineID', default=0)
    fldWeekDays     = models.CharField(db_column='fldWeekDays', max_length=50, default='')
    fldTransferDesk = models.CharField(db_column='fldTransferDesk', max_length=200, default='')
    fldStartTime    = models.CharField(db_column='fldStartTime', max_length=10, default='')
    fldEndTime      = models.CharField(db_column='fldEndTime', max_length=10, default='')
    fldFullTime     = models.CharField(db_column='fldFullTime', max_length=10, default='')
    fldLastMDate    = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM     = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldAirlineID', 'fldWeekDays', 'fldTransferDesk', 'fldStartTime', 'fldEndTime'], name='AirlineOpenTime'),
        ]
        db_table = 'tblairlineopentime'
        ordering = ['fldID']
        unique_together = (('fldAirlineID', 'fldWeekDays', 'fldTransferDesk', 'fldStartTime', 'fldEndTime'),)
    
    def __str__(self):
        return f"Airline ID: {self.fldAirlineID}, Week Days: {self.fldWeekDays}, Transfer Desk: {self.fldTransferDesk}"


class AirlineOpenTimeBackup(models.Model):
    fldID           = models.AutoField(db_column='fldID', primary_key=True)
    fldAirlineID    = models.IntegerField(db_column='fldAirlineID', default=0)
    fldWeekDays     = models.CharField(db_column='fldWeekDays', max_length=50, default='')
    fldTransferDesk = models.CharField(db_column='fldTransferDesk', max_length=200, default='')
    fldStartTime    = models.CharField(db_column='fldStartTime', max_length=10, default='')
    fldEndTime      = models.CharField(db_column='fldEndTime', max_length=10, default='')
    fldFullTime     = models.CharField(db_column='fldFullTime', max_length=10, default='')
    fldLastMDate    = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM     = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldAirlineID', 'fldWeekDays', 'fldTransferDesk', 'fldStartTime', 'fldEndTime'], name='TblAirlineOpenTimeBackup'),
        ]
        db_table = 'tblairlineopentime'
        ordering = ['fldID']
        unique_together = (('fldAirlineID', 'fldWeekDays', 'fldTransferDesk', 'fldStartTime', 'fldEndTime'),)
    
    def __str__(self):
        return f"Airline ID: {self.fldAirlineID}, Week Days: {self.fldWeekDays}, Transfer Desk: {self.fldTransferDesk}"


class BoardingGate(models.Model):
    fldID               = models.AutoField(db_column='fldID', primary_key=True)
    fldNo               = models.CharField(db_column='fldNo', max_length=50, default='')
    fldLeftCoordinate   = models.CharField(db_column='fldLeftCoordinate', max_length=200, default='')
    fldRightCoordinate  = models.CharField(db_column='fldRightCoordinate', max_length=200, default='')
    fldLastMDate        = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM         = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        db_table = 'tblboardinggate'
        indexes = [
            models.Index(fields=['fldNo'], name='boardinggate_fldNo'),
        ]
        ordering = ['fldID']
    
    def __str__(self):
        return f"Gate No: {self.fldNo}, Coordinates: {self.fldLeftCoordinate} - {self.fldRightCoordinate}"


class BoardingGateBackup(models.Model):
    fldID               = models.AutoField(db_column='fldID', primary_key=True)
    fldNo               = models.CharField(db_column='fldNo', max_length=50, default='')
    fldLeftCoordinate   = models.CharField(db_column='fldLeftCoordinate', max_length=200, default='')
    fldRightCoordinate  = models.CharField(db_column='fldRightCoordinate', max_length=200, default='')
    fldLastMDate        = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM         = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        db_table = 'tblboardinggate_backup'
        indexes = [
            models.Index(fields=['fldNo'], name='boardinggatebackup_fldNo'),
        ]
        ordering = ['fldID']

    def __str__(self):
        return f"Gate No: {self.fldNo}, Coordinates: {self.fldLeftCoordinate} - {self.fldRightCoordinate}"


class General(models.Model):
    fldID        = models.AutoField(db_column='fldID', primary_key=True)
    fldName      = models.CharField(db_column='fldName', max_length=200, default='')
    fldType      = models.CharField(db_column='fldType', max_length=200, default='')
    fldValue     = models.TextField(db_column='fldValue', null=True, blank=True)
    fldLastMDate = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM  = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldName'], name='general_fldName'),
        ]
        db_table = 'tblgeneral'
        ordering = ['fldID']

    def __str__(self):
        return f"{self.fldName} ({self.fldType})"

    @property
    def fldValue_short(self):
        # return General.objects.annotate(fldPicture_short=Left('fldValue')).get(pk=self.pk).fldValue_short
        return get_truncated_value(General, 'fldValue', self)

class Tib(models.Model):
    fldID          = models.AutoField(db_column='fldID', primary_key=True)
    fldNo          = models.CharField(db_column='fldNo', max_length=50, default='')
    fldStatus      = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldOrientation = models.CharField(db_column='fldOrientation', max_length=20, default='')
    fldCoordinate  = models.CharField(db_column='fldCoordinate', max_length=200, default='')
    fldPicture     = models.TextField(db_column='fldPicture', null=True, blank=True)
    fldLastMDate   = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM    = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldNo'], name='tib_fldNo'),
        ]
        db_table = 'tbltib'
        ordering = ['fldID']

    def __str__(self):
        return f"TIB No: {self.fldNo}, Status: {self.fldStatus}, Orientation: {self.fldOrientation}, Coors: {self.fldCoordinate}"

    @property
    def fldPicture_short(self):
        return get_truncated_value(Tib, 'fldPicture', self)


class TibBackup(models.Model):
    fldID          = models.AutoField(db_column='fldID', primary_key=True)
    fldNo          = models.CharField(db_column='fldNo', max_length=50, default='')
    fldStatus      = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldOrientation = models.CharField(db_column='fldOrientation', max_length=20, default='')
    fldCoordinate  = models.CharField(db_column='fldCoordinate', max_length=200, default='')
    fldPicture     = models.TextField(db_column='fldPicture', null=True, blank=True)
    fldLastMDate   = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM    = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        managed = False
        indexes = [
            models.Index(fields=['fldNo'], name='tibbackup_fldNo'),
        ]
        db_table = 'tbltib_backup'
        ordering = ['fldID']

    def __str__(self):
        return f"TIB No: {self.fldNo}, Status: {self.fldStatus}, Orientation: {self.fldOrientation}, Coors: {self.fldCoordinate}"

    @property
    def fldPicture_short(self):
        return get_truncated_value(TibBackup, 'fldPicture', self)


class TibEstimationTime(models.Model):
    fldID                  = models.AutoField(db_column='fldID', primary_key=True)
    fldTIBNo               = models.CharField(db_column='fldTIBNo', max_length=50, default='')
    fldTransferNo          = models.CharField(db_column='fldTransferNo', max_length=50, default='')
    fldTimeWithAPM         = models.IntegerField(db_column='fldTimeWithAPM', null=True, blank=True)
    fldDirectionWithAPM    = models.CharField(db_column='fldDirectionWithAPM', max_length=1, default='')
    fldTimeWithoutAPM      = models.IntegerField(db_column='fldTimeWithoutAPM', null=True, blank=True)
    fldDirectionWithoutAPM = models.CharField(db_column='fldDirectionWithoutAPM', max_length=1, default='')
    fldLastMDate           = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM            = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        indexes = [
            models.Index(fields=['fldTIBNo', 'fldTransferNo'], name='tibestimationtime_fldTIBNo'),
        ]
        db_table = 'tbltibestimationtime'
        ordering = ['fldID']
        managed = False

    def __str__(self):
        time_with_apm = f"{self.fldTimeWithAPM} {self.fldDirectionWithAPM}" if self.fldTimeWithAPM is not None and self.fldDirectionWithAPM else "NULL"
        time_without_apm = f"{self.fldTimeWithoutAPM} {self.fldDirectionWithoutAPM}" if self.fldTimeWithoutAPM is not None and self.fldDirectionWithoutAPM else "NULL"
    
        return f"TIB No: {self.fldTIBNo}, Transfer No: {self.fldTransferNo}, TDwAPM: {time_with_apm}, TDwoAPM: {time_without_apm}"

class TibEstimationTimeBackup(models.Model):
    fldID                  = models.AutoField(db_column='fldID', primary_key=True)
    fldTIBNo               = models.CharField(db_column='fldTIBNo', max_length=50, default='')
    fldTransferNo          = models.CharField(db_column='fldTransferNo', max_length=50, default='')
    fldTimeWithAPM         = models.IntegerField(db_column='fldTimeWithAPM', null=True, blank=True)
    fldDirectionWithAPM    = models.CharField(db_column='fldDirectionWithAPM', max_length=1, default='')
    fldTimeWithoutAPM      = models.IntegerField(db_column='fldTimeWithoutAPM', null=True, blank=True)
    fldDirectionWithoutAPM = models.CharField(db_column='fldDirectionWithoutAPM', max_length=1, default='')
    fldLastMDate           = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM            = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        indexes = [
            models.Index(fields=['fldTIBNo', 'fldTransferNo'], name='tibestimationtimebk_fldTIBNo'),
        ]
        db_table = 'tbltibestimationtime'
        ordering = ['fldID']
        managed = False

    def __str__(self):
        time_with_apm = f"{self.fldTimeWithAPM} {self.fldDirectionWithAPM}" if self.fldTimeWithAPM is not None and self.fldDirectionWithAPM else "NULL"
        time_without_apm = f"{self.fldTimeWithoutAPM} {self.fldDirectionWithoutAPM}" if self.fldTimeWithoutAPM is not None and self.fldDirectionWithoutAPM else "NULL"
    
        return f"TIB No: {self.fldTIBNo}, Transfer No: {self.fldTransferNo}, TDwAPM: {time_with_apm}, TDwoAPM: {time_without_apm}"


class TibStatus(models.Model):
    fldID            = models.AutoField(db_column='fldID', primary_key=True)
    fldNo            = models.CharField(db_column='fldNo', max_length=50, default='')
    fldStatus        = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldSendEmail     = models.CharField(db_column='fldSendEmail', max_length=5, default='')
    fldLastLoginTime = models.CharField(db_column='fldLastLoginTime', max_length=50, default='')

    class Meta:
        indexes = [
            models.Index(fields=['fldNo', 'fldStatus'], name='tibstatus_fldNo'),
        ]
        db_table = 'tbltibstatus'
        ordering = ['fldID']
        managed = False

    def __str__(self):
        return f"TIB No: {self.fldNo}, Status: {self.fldStatus}, Send Email: {self.fldSendEmail}, Last Login Time: {self.fldLastLoginTime}"

# Usage:
# transfer_instance = Transfer.objects.get(pk=1)
# print(transfer_instance.fldLeftPicture_short)
# print(transfer_instance.fldRightPicture_short)
class Transfer(models.Model):
    fldID              = models.AutoField(db_column='fldID', primary_key=True)
    fldType            = models.CharField(db_column='fldType', max_length=20, default='')
    fldNo              = models.CharField(db_column='fldNo', max_length=50, default='')
    fldStatus          = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldName            = models.CharField(db_column='fldName', max_length=200, default='')
    fldLeftCoordinate  = models.CharField(db_column='fldLeftCoordinate', max_length=200, default='')
    fldRightCoordinate = models.CharField(db_column='fldRightCoordinate', max_length=200, default='')
    fldLeftPicture     = models.TextField(db_column='fldLeftPicture', null=True, blank=True)
    fldRightPicture    = models.TextField(db_column='fldRightPicture', null=True, blank=True)
    fldStartTime       = models.CharField(db_column='fldStartTime', max_length=10, default='')
    fldEndTime         = models.CharField(db_column='fldEndTime', max_length=10, default='')
    fldFullTime        = models.CharField(db_column='fldFullTime', max_length=10, default='')
    fldLastMDate       = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM        = models.CharField(db_column='fldEmpNameM', max_length=250, default='')

    class Meta:
        indexes = [
            models.Index(fields=['fldType', 'fldNo', 'fldStatus'], name='transfer_fldType'),
        ]
        db_table = 'tbltransfer'
        ordering = ['fldID']
        managed = False

    @property
    def fldLeftPicture_short(self):
        return get_truncated_value(Transfer, 'fldLeftPicture', self)

    @property
    def fldRightPicture_short(self):
        return get_truncated_value(Transfer, 'fldRightPicture', self)

    def __str__(self):
        return f"Transfer No: {self.fldNo}, Type: {self.fldType}, Status: {self.fldStatus}, Name: {self.fldName}"


class TransferBackup(models.Model):
    fldID              = models.AutoField(db_column='fldID', primary_key=True)
    fldType            = models.CharField(db_column='fldType', max_length=20, default='')
    fldNo              = models.CharField(db_column='fldNo', max_length=50, default='')
    fldStatus          = models.CharField(db_column='fldStatus', max_length=20, default='')
    fldName            = models.CharField(db_column='fldName', max_length=200, default='')
    fldLeftCoordinate  = models.CharField(db_column='fldLeftCoordinate', max_length=200, default='')
    fldRightCoordinate = models.CharField(db_column='fldRightCoordinate', max_length=200, default='')
    fldLeftPicture     = models.TextField(db_column='fldLeftPicture', null=True, blank=True)
    fldRightPicture    = models.TextField(db_column='fldRightPicture', null=True, blank=True)
    fldStartTime       = models.CharField(db_column='fldStartTime', max_length=10, default='')
    fldEndTime         = models.CharField(db_column='fldEndTime', max_length=10, default='')
    fldFullTime        = models.CharField(db_column='fldFullTime', max_length=10, default='')
    fldLastMDate       = models.DateTimeField(db_column='fldLastMDate', default='0001-01-01 00:00:00')
    fldEmpNameM        = models.CharField(db_column='fldEmpNameM', max_length=250, default='')


    class Meta:
        indexes = [
            models.Index(fields=['fldType', 'fldNo', 'fldStatus'], name='transferbackup_fldType'),
        ]
        db_table = 'tbltransfer_backup'
        ordering = ['fldID']
        managed = False

    @property
    def fldLeftPicture_short(self):
        return get_truncated_value(Transfer, 'fldLeftPicture', self)

    @property
    def fldRightPicture_short(self):
        return get_truncated_value(Transfer, 'fldRightPicture', self)

    def __str__(self):
        return f"Transfer No: {self.fldNo}, Type: {self.fldType}, Status: {self.fldStatus}, Name: {self.fldName}"
