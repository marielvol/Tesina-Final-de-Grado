<?php
$target_dir = "images/";
$target_file = $target_dir . basename($_FILES["uploaded_image"]["name"]);
move_uploaded_file($_FILES["uploaded_image"]["tmp_name"], $target_file);

$python_script = "python_scripts/cancer_detection_script.py";
$command = "python3 $python_script $target_file";
$output = shell_exec($command);

$result_image = "processed_images/result.jpg";
?>

<!DOCTYPE html>
<html>
<head>
    <title>Resultado de Detección</title>
</head>
<body>
    <h1>Resultado de Detección</h1>
    <img src="<?php echo $result_image; ?>" alt="Resultado">
</body>
</html>
