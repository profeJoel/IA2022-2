# RESULTADOS DE EXPERIMENTOS

# Estado Inicial = "87653H241"

$\left[\begin{array}{ccc}
    8 & 7 & 6\\
    5 & 3 & H\\
    2 & 4 & 1
\end{array}\right]$


<!--
|Metrics/Algorithms|DFS|Better First|Hill Climbing|Beam Search (B=2)|Beam Search (B=1)|
|-----|-----|-----|-----|-----|-----|
|Discovered|1217|169|16|158183|169|
|To Explore|534|74|7|16192|1|
|Iterations|684|96|8|134062|96|
|Quality (level)|665|95|X|29|95|
-->

|Algorithms/Metrics|Discovered|To Explore|Iterations|Quality (level)|
|-----|-----|-----|-----|-----|
|BFS| na | na | na | na |
|DFS|1217|534|684|665|
|Better First|169|74|96|95|
|Hill Climbing|16|7|8|X|
|Beam Search (B=2)|158183|16192|134062|29|
|Beam Search (B=1)|169|1|96|95|
|Beam Search (B=50%)|8853|412|5276|71|
|Beam Search (B=25%)|169|1|96|95|