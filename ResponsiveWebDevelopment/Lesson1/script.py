for i in range(552):
    with open(f"pages/{i}.html", "w") as page:
        page.write(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter {i}</title>
    <link rel="icon" type="image/png" sizes="32x32" href="../favicon32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="../favicon16.png" />
    <script
    type="module"
    src="https://cdn.jsdelivr.net/gh/zerodevx/zero-md@2/dist/zero-md.min.js"
  ></script>
    <link rel="stylesheet" href="../style.css" />
</head>
<body>
    <zero-md src="../chapters/{i}.md">
    <template>
        <link rel="stylesheet" href="../mdstyle.css" />
      </template>
    </zero-md>
</body>
</html>                         
""")
        