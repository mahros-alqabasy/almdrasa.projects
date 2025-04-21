import tkinter as tk

class SyntaxHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.tag_configure('keyword', foreground='blue')
        self.text_widget.tag_configure('string', foreground='green')
        self.text_widget.tag_configure('comment', foreground='gray')
        self.highlight_syntax()

    def highlight_syntax(self):
        content = self.text_widget.get('1.0', 'end-1c')
        self._apply_tag(content, r'\b(def|class|import|from|as)\b', 'keyword')
        self._apply_tag(content, r'".*?"', 'string')
        self._apply_tag(content, r'#.*$', 'comment')

    def _apply_tag(self, content, pattern, tag):
        import re
        for match in re.finditer(pattern, content):
            self.text_widget.tag_add(tag, f'1.0 + {match.start()} chars', f'1.0 + {match.end()} chars')
