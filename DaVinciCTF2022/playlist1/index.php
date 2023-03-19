<!DOCTYPE html>
<html>

<head>
    <title>My Top 5</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" integrity="sha384-ekOryaXPbeCpWQNxMwSWVvQ0+1VrStoPJq54shlYhR8HzQgig1v5fas6YgOqLoKz" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
</head>




<?php
if (isset($_GET['MyTop5'])) {
    $top = $_GET['MyTop5'];
} else {
    $top = "1";
}

if (isset($_GET['playlistTop'])) {
    $playlist = $_GET['playlistTop'];
} else {
    $playlist = "TopRapUS";
}


if (isset($playlist) && isset($top)) {
    $handle = fopen($playlist, "r");
    if ($handle) {
        $tag = "";
        $counter = 0;
        while (($line = fgets($handle)) !== false) {
            if ($counter + 1 == $top) {
                $tag = $line;
            }
            $counter++;
        }
        fclose($handle);
    }
}
?>
<div class="p-4 text-center bg-image" >
    <div class="text-center">
        <br>

        <h1><b><u>Top Songs</u></b></h1>
    
        <br>
   
        <br>
        <br>

        <body>
            <h2><b>Song</b></h2>
            <form method="get">
                <input type="radio" id="video1" name="MyTop5" value="1" <?php if( !(isset($_GET['MyTop5'])) || (isset($_GET['MyTop5']) && $_GET['MyTop5'] == '1')) echo ' checked="checked"'?>>
                <label for="video1">Top 1</label>

                <input type="radio" id="video2" name="MyTop5" value="2" <?php if( (isset($_GET['MyTop5']) && $_GET['MyTop5'] == '2')) echo ' checked="checked"'?>>
                <label for="video2">Top 2</label>

                <input type="radio" id="video3" name="MyTop5" value="3" <?php if( (isset($_GET['MyTop5']) && $_GET['MyTop5'] == '3')) echo ' checked="checked"'?>>
                <label for="video3">Top 3</label>

                <input type="radio" id="video4" name="MyTop5" value="4" <?php if( (isset($_GET['MyTop5']) && $_GET['MyTop5'] == '4')) echo ' checked="checked"'?>>
                <label for="video4">Top 4</label>

                <input type="radio" id="video5" name="MyTop5" value="5" <?php if( (isset($_GET['MyTop5']) && $_GET['MyTop5'] == '5')) echo ' checked="checked"'?>>
                <label for="video5">Top 5</label>

                <br>
                <br>

                <h2><b>Playlist</b></h2>

                <form method="post">
                    <input type="radio" id="TOP" name="playlistTop" value="TopRapUS" <?php if( !(isset($_GET['playlistTop'])) || (isset($_GET['playlistTop']) && $_GET['playlistTop'] == 'TopRapUS')) echo ' checked="checked"'?>>
                    <label for="video1">Rap US</label>

                    <input type="radio" id="TOP" name="playlistTop" value="TopRapFr" <?php if((isset($_GET['playlistTop']) && $_GET['playlistTop'] == 'TopRapFr')) echo ' checked="checked"'?>>
                    <label for="video2">Rap FR </label>
                    <br>
                    <br>
                    <div>
                        <button class="btn btn-dark" type="submit">Submit</button>
                    </div>
                </form>

            </form>

        </body>
        <br>
    </div>
</div>
</div>
</html>

