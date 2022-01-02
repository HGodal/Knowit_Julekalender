# Dag 17: [Robotstøvsugeren]()

Alvene har kjøpt Julenissen og Julenissemor en robotstøvsuger i presang, slik at de kan bruke litt mindre tid på å holde reint hjemme og litt mer tid på å opprettholde det endeløse blodtørstige slaveriet som er kapitalismen uutømmelige sult for julegaver.

Støvsugeren har følgende form:

```
  sss  
 sssss 
sssssss
sssssss
sssssss
 sssss 
  sss  
```

Videre har støvsugeren koster som gjør at den kan rengjøre følgende areal under seg:

```
kkk   kkk
kkkkkkkkk
kkkkkkkkk
 kkkkkkk 
 kkkkkkk 
 kkkkkkk 
kkkkkkkkk
kkkkkkkkk
kkk   kkk
```

Kostearealet dekker et større området enn plassen selve roboten tar opp.


## Oppgave

Gitt [følgende kart](kart.txt) der `x` markerer områder roboten ikke kan kjøre gjennom og  `(mellomrom)` er skittent gulvareal. Hvor mange ruter av gulvet forblir skitne etter roboten har kjørt (og... teleportert?) overalt hvor den kan?

Du kan anta at roboten klarer å navigere på magisk vis til alle områder i kartet hvor den får fysisk plass. Kostene er immaterielle og blir ikke påvirket av vegger, de kan altså sveipe gulvet på andre siden av en vegg (ikke spør hvordan).

## Eksempel

Her er et ferdig rengjort kart der `.` markerer rengjort areal. Dette kartet har 96 skitne ruter etter rengjøring.

```
xxxxxxxxxxxxxxxxxxxx
x ..x..........  x x
x.xxx..........  xxx
x.............  x  x
x.............     x
x.............     x
x............xx    x
x............xx    x
x............xx    x
x............xx    x
x............xx    x
xxxxxx.......xx    x
x  ...........     x
x   ..........     x
x   ..........     x
x   ..........     x
x  .......xxxxxxxxxx
x  ..x...xxxxx     x
x  ...   ...       x
xxxxxxxxxxxxxxxxxxxx
```
