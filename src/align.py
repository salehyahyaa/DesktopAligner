import subprocess

script = '''
tell application "Finder"
    set sel to selection
    if sel is {} then return

    -- build list of {item, y}
    set itemData to {}
    repeat with itemRef in sel
        set {xVal, yVal} to position of itemRef
        set end of itemData to {itemRef, yVal}
    end repeat

    -- sort by Y (top to bottom)
    set sortedItems to my sortByY(itemData)

    -- anchor to topmost item
    set firstPair to item 1 of sortedItems
    set topItem to item 1 of firstPair
    set {xPos, yStart} to position of topItem

    set spacing to 100
    set i to 0

    repeat with pair in sortedItems
        set itemRef to item 1 of pair
        set newY to yStart + (i * spacing)
        set position of itemRef to {xPos, newY}
        set i to i + 1
    end repeat
end tell

-- AppleScript sort function
on sortByY(itemList)
    set sortedList to {}
    repeat until itemList is {}
        set lowest to item 1 of itemList
        repeat with i from 1 to count of itemList
            if item 2 of item i of itemList < item 2 of lowest then
                set lowest to item i of itemList
            end if
        end repeat
        set end of sortedList to lowest
        set itemList to my removeItem(lowest, itemList)
    end repeat
    return sortedList
end sortByY

on removeItem(theItem, theList)
    set newList to {}
    repeat with i from 1 to count of theList
        if item i of theList is not theItem then
            set end of newList to item i of theList
        end if
    end repeat
    return newList
end removeItem
'''

subprocess.run(["osascript", "-e", script])