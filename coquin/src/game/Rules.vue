

<template>

<v-container pa-0>
    <v-img max-width="200" src="../assets/logo.svg"></v-img>
    <v-spacer class="pt-4"></v-spacer>

    <p class="font-weight-thin">
        <v-tooltip bottom>
            <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" x-large href="https://github.com/sweet-cookies/coquin">
                    <v-icon color="grey lighten-1">mdi-github-circle</v-icon>
                </v-btn>github.com/sweet-cookies/coquin
            </template>
            <span>View on github</span>
        </v-tooltip>
    </p>

    <h1>Mise en place</h1>
    <p>Avant de commencer une partie, prenez le temps de lire la règle pour configurer le jeu.</p>
    <p>Ce jeu est constitué de plusieurs étapes. Lors d'une partie vous pouvez utiliser une ou toutes les étapes.
        <br> Une étape est constituée d'un deck. Les différents decks allant de la découverte pour une première rencontre avec de nouveaux partenaires, à des decks plus hot pour pimenter un moment coquin entre personnes complices.</p>

    <p>Vous pouvez vous laisser guider par le jeu ou encore l’utiliser comme support et laisser place à votre imagination et vos désirs.</p>

    <p>Une partie par défaut est composée de 3 étapes. soft, coquine et hot et un deck de positions. Lors d'une partie vous pouvez utiliser ou non ces 3 étapes.</p>

    <v-alert color="warning" dense border="left" elevation="2" colored-border icon="mdi-school">
        <p><b>Important</b>, suivant vos envies, votre complicité et le nombre de participants, certains decks peuvent ne pas être adaptés. Prenez le temps de bien les choisir avant de lancer une partie.</p>
    </v-alert>

    <p>Rien n'est obligatoire, vous pouvez passer des gages, en piocher d'autres ou laisser libre court à votre imagination pour adapter les gages ou les règles en cours de jeu suivant vos envies et le nombre de participants.</p>

    <v-alert color="blue-grey" dense border="left" elevation="2" colored-border icon="mdi-school">
        <p class="font-italic">

            lors d’une partie pour faire connaissance avec de nouveaux partenaires, vous pouvez, par exemple, vous contentez de faire une partie avec le deck soft uniquement En revanche, pour un couple, un deck soft peut être un bon préliminaire avant de passer au
            deck suivant quand la température monte.
            <br>Pour ceux qui aiment les règles, vous pouvez définir un nombre de tour avant de changer de deck, par exemple : passer à une étape plus hot après 20 tours.
        </p>
    </v-alert>
    <p>Prenez le temps de connaitre les envies de chacun pour sélectionner le ou les decks. Certains decks sont adaptés pour faire connaissance et d'autres à l'opposé demandent une bonne connaissance et complicité avec votre partenaire.
    </p>


    <h1>Déroulement</h1>
    <p>Lors d'un tour standard, il sera désigné un gagnant et un perdant. Chaque tour, le perdant tire une carte gage et réalise l'action indiquée. Sur l'application, cliquer sur <kbd>suivant</kbd> et sélectionnez le nom du perdant. Puis laissez le tirer
        une carte gage et la réaliser.</p>
    <p>Pour connaître qui est le gagnant et le perdant, vous avez le choix entre plusieurs modes, voir ci dessous.</p>

    <h1>Les differents modes</h1>
    <p>
        <ul>
            <li><kbd class="font-weight-medium">Standard</kbd> : Lancer des dés ou tirer des cartes d'un jeu classique. Le perdant est le joueur avec le plus petit score, le gagnant sera le joueur avec le plus haut score. Si vous n'avez pas cela, utiliser
                tout moyen qui vous passe par la tête pour désigner un gagnant et un perdant.</li>
            <li><kbd class="font-weight-medium">Standard 3 et plus</kbd> : Similaire à la règle standard, lancer 4 dés (ou tirez 4 cartes), le score le plus haut est le gagnant. Le plus bas est le perdant.</li>
            <li><kbd class="font-weight-medium">Chacun son tour</kbd> : Chacun son tour, un joueur tire une carte gage, il est considéré comme perdant.</li>
            <li><kbd class="font-weight-medium">Chacun son tour 3 et plus</kbd> : Similaire à la règle Chacun son tour. Tirez au sort par un lancé de dés ou tirage de carte pour déterminer le gagnant parmis les joueurs restants.</li>
            <li><kbd class="font-weight-medium">Aléatoire</kbd> : Un perdant est défini aléatoirement chaque tour.</li>
            <li><kbd class="font-weight-medium">Aléatoire à 3 et plus</kbd> : Similaire à la règle random. Tirez au sort par un lancé de dés ou tirage de carte pour déterminer le gagnant parmis les joueurs restants.</li>
        </ul>
    </p>

    <h1>Fin de partie</h1>

    <p>Ajoutez un peu de piquant à une partie, le gagnant de la partie donne un défi au perdant à réaliser dans la semaine. Un diner, un massage, une sortie, un cadeau ou quelque chose de plus hot. Soyez inventif, faites vous plaisir.</p>

    <p>Il y a 2 conditions pour arriver en fin de partie :</p>
    <p>
        <ul>
            <li>Quand l'un des joueurs a joui. Il devient un serviteur et doit faire ce que lui demande le ou les autres joueurs.</li>
            <li>Un joueur pioche une carte fin de partie : vous devez réaliser le gage indiqué sur la carte jusqu'à ce qu'un joueur devienne serviteur. Si cette carte arrive trop tôt dans la partie, vous pouvez choisir de la remettre dans le deck et continuer
                le jeu.</li>
        </ul>
    </p>
    <v-alert color="blue-grey" dense border="left" elevation="2" colored-border icon="mdi-school">
        <p class="font-italic">Dans le cas de 3 joueurs et plus, libre à vous d'adapter les cartes fin de partie pour réaliser le gage à plusieurs ou en changeant de partenaire tour à tour jusqu'à la fin.</p>
    </v-alert>
    <p>La partie se termine quand vous le souhaitez ! Libre à vous de continuer à vous amuser lorsque tous les joueurs ont joui ou non.</p>

    <p>Voici quelques suggestions de déroulement de fin de partie :</p>
    <p>
        <ul>
            <li><kbd class="font-weight-medium">2 joueurs</kbd> : un joueur a joui, il devient serviteur. L’autre joueur peut lui demander de le faire jouir de la façon qu'il souhaite.</li>
            <li><kbd class="font-weight-medium">3 joueurs</kbd> : un joueur a joui, il devient serviteur. Vous pouvez lui demander de l'aide pour faire jouir les autres joueurs ensemble, tour à tour ou Il peut simplement regarder les autres joueurs finir
                devant lui.</li>
            <li><kbd class="font-weight-medium">4 joueurs</kbd> : un joueur a joui, il devient serviteur. Vous pouvez continuer la partie en sollicitant l'aide du serviteur pour vos gages, ou tous profiter de l'aide du serviteur pour vous satisfaire.</li>
        </ul>
    </p>

    <h1>Quelques précisions</h1>
    <p>Si une carte gage n’est pas jouable, exemple : doit être réalisée sur une femme et que le joueur ciblé est un homme ou retirer un vêtement sur un joueur qui n’en a déjà plus. La majorité décide d’adapter le gage, le réaliser sur un autre joueur ou
        simplement en piocher un autre.</p>
    <p>Dans les cas où le perdant et le gagnant d’un tour ne sont pas attirés sexuellement l’un envers l’autre, le gagnant peut prendre le joueur suivant en partant toujours du score le plus petit.</p>
    <p>En cas d'égalité à 2 joueurs, relancer les dés. Pour 3 joueurs ou plus, le premier lancé est votre score. Ensuite relancez les dés uniquement avec les personnes qui ont fait le même score pour définir votre position par rapport à celle ci. Dans le
        cas d'une égalité pour définir un perdant, le gagnant peut choisir le perdant ou demander de relancer les dés.
    </p>
    <p>
        Si un gage implique plus de 2 personnes, c'est le perdant ainsi que le joueur suivant avec le score le plus petit qui le réalisent sur le gagnant.
    </p>
    <p>
        Si vous tirez un gage ou position que vous ne pouvez pas réaliser, vous pouvez l'adapter ou en piocher un autre. Le but est que tout le monde s'amuse.
        <br> Vous pouvez également laisser d'autres joueurs le réaliser à votre place, profitez du spectacle ...
    </p>

    <h1>Variantes</h1>
    <p>
        <kbd class="font-weight-medium">Plus de fun à 4</kbd> : Jetez 4 dés, les gagnants sont les 2 joueurs avec le score le plus haut. Les 2 autres sont les perdants.
        <br> Le joueur avec le score le plus petit tire une carte gage. Il devra le réaliser sur le joueur avec le score le plus haut. Quant au deuxième perdant, il réalisera ce même gage sur le deuxième gagnant.
        <br> Dans le cas où un binôme de gagnant/perdant n'a pas d'attirances sexuelles, le joueur avec le score le plus haut choisi d'échanger ou non de perdant. Dans le cas contraire, il réalise le gage avec son perdant assigné pendant que les autres regardent
        (ou se joignent s’ils sont conviés au gage).
    </p>

    <p>
        <kbd class="font-weight-medium">En équipe</kbd> : Faites des équipes de 2 personnes, chaque équipe lance une partie en duo. Découvrez quelle sera la dernière équipe encore en jeu. Bien sûr vous pouvez vous immiscer dans les gages d’autres équipes
        pour essayer de remporter la partie :)
    </p>

    <p>
        <kbd class="font-weight-medium">Gagnant roi</kbd> : le perdant tire un gage et c'est le gagnant qui décide avec qui (lui compris) le perdant doit le réaliser.
    </p>

    <p>
        <kbd class="font-weight-medium">Positions</kbd> : Tirez des positions et réaliser les pendant 3 minutes jusqu'à atteindre votre limite.
    </p>

    <p>
        <kbd class="font-weight-medium">Le soumis</kbd> : bandez les yeux d’un joueur, vous pouvez également l’attacher pour plus de plaisir.
        <br> Tirez des cartes gages une par une et réalisez les sur ce joueur, le but est de lui donner du plaisir en se laissant porter par les différentes surprises.
    </p>

</v-container>

</template>

<script>

export default {
    name: 'Rules',
    props: {},
    mounted() {},
    watch: {},
    methods: {},
    data: () => ({}),
};

</script>
