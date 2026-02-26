from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Developer Cheat Sheet', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Terminal Basics
pdf.chapter_title('Terminal Basics')
terminal_text = (
    "ls / dir: List files in current directory\n"
    "cd <dir>: Change directory\n"
    "mkdir <dir>: Create a new directory\n"
    "rm <file> / rmdir <dir>: Remove files or directories\n"
    "cat <file> / type <file>: Display file content\n"
    "curl <url>: Transfer data from or to a server\n"
)
pdf.chapter_body(terminal_text)

# Git Commands
pdf.chapter_title('Git Commands')
git_text = (
    "git init: Initialize a new Git repository\n"
    "git add <file>: Add file contents to the index\n"
    "git commit -m \"message\": Record changes to the repository\n"
    "git status: Show the working tree status\n"
    "git log: Show commit logs\n"
    "git diff: Show changes between commits, commit and working tree, etc\n"
)
pdf.chapter_body(git_text)

# How to run tests
pdf.chapter_title('How to Run Tests')
test_text = (
    "Python:\n"
    "  pytest: Run all tests in current directory\n"
    "  python -m unittest: Run unit tests\n\n"
    "JavaScript/Node:\n"
    "  npm test: Run test script defined in package.json\n"
)
pdf.chapter_body(test_text)

pdf.output('dev_cheat_sheet.pdf', 'F')
print("PDF generated successfully.")
