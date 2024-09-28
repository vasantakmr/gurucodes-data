---
title: "Automating Excel: Introduction to Macros & VBA [Week 18]"
---

### 5.1 Introduction to Macros
Macros allow you to automate repetitive tasks in Excel by recording a series of actions.
- **Recording a Macro**:  
  Go to `View > Macros > Record Macro`. Perform a task, then stop recording, and Excel will generate a script for that action.

### 5.2 Introduction to VBA (Visual Basic for Applications)
**VBA** is Excel’s programming language that allows you to write your own scripts and automate complex tasks beyond what macros can handle.
- **Writing Simple VBA**:  
  Go to `Developer > Visual Basic` and start writing your VBA scripts.

#### Example:
Write a simple macro that formats all the sheets in your workbook:
```vba
Sub FormatSheets()
    Dim ws As Worksheet
    For Each ws In ThisWorkbook.Sheets
        ws.Cells.Font.Name = "Arial"
        ws.Cells.Font.Size = 12
    Next ws
End Sub
```
