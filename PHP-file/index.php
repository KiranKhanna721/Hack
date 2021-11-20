<?php
	// get files in the current directory
	$files = scandir( getcwd() );
?>
<!DOCTYPE html>
<html>
	<head>
		<title>
            Hello world.php
		</title>

		<meta charset="utf-8">
		<meta name="title" content="a" />
	</head>
	<body>
		<h1>
			INDEX try
		</h1>
		<hr />
		<ul>
			<?php foreach ( $files as $file ) : ?>
				<?php if ( '.' != $file && '..' != $file && '.git' != $file && 'README.md' != $file && '.htaccess' != $file ) : ?>
					<li>
						<a href="<?php echo $file; ?>">
							<?php echo $file; ?>
						</a>
					</li>
				<?php endif; ?>
			<?php endforeach; ?>
		</ul>
		<hr />
	</body>
</html>