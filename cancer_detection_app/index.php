<!DOCTYPE html>
<html>
<head>
    <title>Detección de Cáncer de Colon</title>
    <style>
        h1 {
            text-align: left;
        }

        form {
            text-align: left;
        }

        input[type="file"] {
            display: none;
        }

        .button-container {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .custom-button {
            background-color: orange;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }

        .custom-button:hover {
            background-color: darkorange;
        }

        #image-preview {
            max-width: 100%;
            display: none;
        }
    </style>
    <script>
        function previewImage(input) {
            var preview = document.getElementById('image-preview');
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                }

                reader.readAsDataURL(input.files[0]);
            }
        }
    </script>
</head>
<body>
    <h1>Detección de Cáncer de Colon</h1>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <label for="uploaded_image" class="custom-button">Seleccionar Archivo</label>
        <input type="file" name="uploaded_image" id="uploaded_image" style="display:none;" onchange="previewImage(this);">
        <div class="button-container">
            <input type="submit" value="Cargar y Procesar" class="custom-button">
        </div>
        <img id="image-preview" alt="Vista Previa de la Imagen" src="">
    </form>
</body>
</html>
