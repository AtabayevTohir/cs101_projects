def analyze_fines(filename):
    genre_totals = {}
    severe_books = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                title, genre, DaysOverdue, FinePerDay = line.strip().split(',')
                DaysOverdue = int(DaysOverdue)
                FinePerDay = float(FinePerDay)
                TotalFine = DaysOverdue * FinePerDay
                genre_totals[genre] = genre_totals.get(genre, 0) + TotalFine
                if DaysOverdue > 30:
                    severe_books.append((title, DaysOverdue))
            except (ValueError, IndexError):
                continue
        return genre_totals, severe_books

def save_fine_report(genre_totals, severe_books):
    with open('fine_report.txt', 'w') as report:
        report.write("GENRE FINE REVENUE\n")
        report.write("------------------\n")
        for genre, total in genre_totals.items():
            report.write(f"{genre}: ${total:.2f}\n")
        report.write("\nSEVERE DELAYS (> 30 Days)\n")
        report.write("------------------------\n")
        for title, days in severe_books:
            report.write(f"{title} ({days} days)\n")

def main():
    genre_totals, severe_books = analyze_fines('overdue_log.txt')
    save_fine_report(genre_totals, severe_books)

main()
