# CPW - Engine book h

Source: https://www.chessprogramming.org/CPW_-_Engine_book_h

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* [CPW-Engine](/CPW-Engine "CPW-Engine") \* Book.h**

This is the header file for [CPW-Engine\_book](/CPW-Engine_book "CPW-Engine book")

```
void readBookFile();
void book_addline( int line_no, char * movestring);
int book_add( char * movestring);
int book_present( char * movestring );
int book_getMaxFreq();
void book_loadInternal();
```

**[Up one Level](/CPW-Engine "CPW-Engine")**