from django.db import models


class Snack(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    submitted_by = models.CharField(max_length=100, default="익명")
    created_at = models.DateTimeField(auto_now_add=True)

    def agree_count(self):
        return self.votes.filter(vote_type="agree").count()

    def disagree_count(self):
        return self.votes.filter(vote_type="disagree").count()

    def total_votes(self):
        return self.votes.count()

    def agree_percent(self):
        total = self.total_votes()
        if total == 0:
            return 0
        return round(self.agree_count() / total * 100)

    def __str__(self):
        return self.name


class Vote(models.Model):
    VOTE_CHOICES = [("agree", "동의"), ("disagree", "비동의")]
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE, related_name="votes")
    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["snack", "session_key"]

    def __str__(self):
        return f"{self.snack.name} - {self.vote_type}"
