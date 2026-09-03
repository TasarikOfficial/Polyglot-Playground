import Foundation
let tasks = Array(CommandLine.arguments.dropFirst())
guard !tasks.isEmpty else { print("Usage: swift focus.swift task1 task2 ..."); exit(0) }
let session = 25
print("Focus plan · \(tasks.count * session) minutes")
for (index, task) in tasks.enumerated() {
    print("\(index + 1). \(task) — \(session) min")
}
