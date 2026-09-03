Console.Write("Completed days (example 1,1,1,0,1): ");
var days = (Console.ReadLine() ?? "").Split(',').Select(x => x.Trim() == "1");
int current = 0, best = 0;
foreach (var done in days) { current = done ? current + 1 : 0; best = Math.Max(best, current); }
Console.WriteLine($"Best streak: {best} day(s)");
