# Initialization Routine

Source: https://www.chessprogramming.org/Initialization_Routine

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Evaluation Function Draft](/Evaluation_Function_Draft "Evaluation Function Draft") \* Initialization Routine**

```
int diag_nw[64] = {
   0, 1, 2, 3, 4, 5, 6, 7,
   1, 2, 3, 4, 5, 6, 7, 8,
   2, 3, 4, 5, 6, 7, 8, 9,
   3, 4, 5, 6, 7, 8, 9,10,
   4, 5, 6, 7, 8, 9,10,11,
   5, 6, 7, 8, 9,10,11,12,
   6, 7, 8, 9,10,11,12,13,
   7, 8, 9,10,11,12,13,14
};

int diag_ne[64] = {
   7, 6, 5, 4, 3, 2, 1, 0,
   8, 7, 6, 5, 4, 3, 2, 1,
   9, 8, 7, 6, 5, 4, 3, 2,
  10, 9, 8, 7, 6, 5, 4, 3,
  11,10, 9, 8, 7, 6, 5, 4,
  12,11,10, 9, 8, 7, 6, 5,
  13,12,11,10, 9, 8, 7, 6,
  14,13,12,11,10, 9, 8, 7
};

int bonus_dia_distance[14] = {5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

/* initializes the table of distances between squares */
void setDist() {
   int i,j;

   /* basic distance table used to generate separate tables for pieces */
   for (i = 0; i < 64; ++i) {
      for (j = 0; j < 64; ++j) {
         dist_bonus[i][j] = 14 - ( abs( COL(i) - COL(j) ) + abs( ROW(i) - ROW(j) ) );

         qk_dist[i][j]  = (dist_bonus[i][j] * 5) / 2;
         rk_dist[i][j]  =  dist_bonus[i][j] / 2;
         nk_dist[i][j]  =  dist_bonus[i][j];
         /* bk_dist[i][j] takes into account the numbers of the diagonals */
         bk_dist[i][j]  = dist_bonus[i][j] / 2;
         kb_dist[i][j] += bonus_dia_distance[abs(diag_ne[i] - diag_ne[j])];
         kb_dist[i][j] += bonus_dia_distance[abs(diag_nw[i] - diag_nw[j])];
      }
   }
}
```

**[Up one Level](/Evaluation_Function_Draft "Evaluation Function Draft")**