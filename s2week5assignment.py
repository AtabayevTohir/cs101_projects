from abc import ABC, abstractmethod


class Criterion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def judge(self, value):
        ...

    def evaluate(self, value):
        if self.judge(value):
            status = "PASS"
        else:
            status = "FAIL"

        print(f"[{status}] {self.name}: {value}")
        result = self.judge(value)
        return result


class MinWordsCriterion(Criterion):
    def __init__(self, min_words):
        super().__init__(f"MinWords({min_words})")
        self.min_words = min_words

    def judge(self, value):
        words = value.split()
        result = len(words)>= self.min_words
        return result


class MaxLengthCriterion(Criterion):
    def __init__(self, max_len):
        super().__init__(f"MaxLength({max_len})")
        self.max_len = max_len

    def judge(self, value):
        result = len(value) <=self.max_len
        return result


class NoBannedWordsCriterion(Criterion):
    def __init__(self, banned):
        super().__init__("NoBannedWords")
        self.banned = banned

    def judge(self, value):
        text = value.lower()
        for word in self.banned:
            if word in text:
                result = False
                return result
        result = True
        return result


class EndsWithPunctuationCriterion:
    def __init__(self):
        self.name = "EndsWithPunctuation"

    def judge(self, value):
        if value and value[-1] in ".!?":
            result = True
        else:
            result = False
        return result

    def evaluate(self, value):
        passed = self.judge(value)
        if passed:
            status = "PASS"
        else:
            status = "FAIL"
        print(f"[{status}] {self.name}: {value}")
        result = passed
        return result


class ModerationReport:
    def __init__(self):
        self.entries = []

    def add(self, criterion_name, value, passed):
        self.entries.append((criterion_name, value, passed))

    def summary(self):
        total = len(self.entries)
        passed = 0
        for entry in self.entries:
            if entry[2]:
                passed += 1
        failed = total - passed
        print(f"Total: {total}, Passed: {passed}, Failed: {failed}")

class ReviewField:
    def __init__(self, field_name):
        self.field_name = field_name
        self.criteria = []
        self.report = ModerationReport()

    def add_criterion(self, criterion):
        self.criteria.append(criterion)

    def moderate(self, value):
        print(f'Moderating {self.field_name}: "{value}"')
        all_passed = True
        for c in self.criteria:
            passed = c.evaluate(value)
            self.report.add(c.name, value, passed)
            if not passed:
                all_passed = False
        result = all_passed
        return result

    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        self.report.summary()

review = ReviewField('comment')
review.add_criterion(MinWordsCriterion(3))
review.add_criterion(MaxLengthCriterion(50))
review.add_criterion(NoBannedWordsCriterion(['spam', 'fake']))
review.add_criterion(EndsWithPunctuationCriterion())

valid1 = review.moderate('Great product overall!')
print(f'Valid: {valid1}')
print()

valid2 = review.moderate('ok')
print(f'Valid: {valid2}')
print()

valid3 = review.moderate('This is spam content')
print(f'Valid: {valid3}')
print()

review.show_report()

try:
    c = Criterion('test')
except TypeError:
    print('Cannot instantiate abstract class')