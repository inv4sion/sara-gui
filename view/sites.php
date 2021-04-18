<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/main.css">
    <link href="https://fonts.googleapis.com/css2?family=Chelsea+Market&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Dosis&display=swap" rel="stylesheet">
    <link rel="icon" href="../archives/logo.ico">
    <title>Inv4sion</title>
    <style>
        .middle{
            color: white;
        }
    </style>
</head>
<body>
    <div class="head">
        <h1>Inv4sion</h1>
    </div>
    <div class="middle">
        <?php
            $myfile = fopen('../archives/site.txt', 'r');
            while(!feof($myfile)) {
                echo fgets($myfile) . "<br>";
              }
            fclose($myfile);
        ?>
    </div>
</body>
<script src="js/main.js"></script>
</html>