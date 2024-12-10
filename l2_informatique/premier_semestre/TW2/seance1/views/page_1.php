<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Premier exercice PHP</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
    </head>
    <body>
        <header>
            <h1>Premier exercice PHP</h1>
            <h2>Réalisé par <span class="nom">Lesaffre maeva</span></h2>
        </header>
        <!-- section résultat. Créer une section pour chaque question -->
        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p>Nous sommes le <?= date('d / m / Y') ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= AfficheVar(4,'go') ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= nparag('test ', 3) ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= diminue('Alors?') ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= diminue2('Alors?') ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= tableMultiplication(2) ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= tablesMultiplications() ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= tablesMultiplications2() ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= separe("Et qu'on sorte+ Vistement : +Car Clément + Le vous mande.") ?></p>
        </section>

        <section>
            <h2>Question <?= $num_quest++ ?></h2>
            <p> <?= "<p>".enSpan("Dupont - Durand")."</p>" ?></p>
        </section>

    </body>

</html>
