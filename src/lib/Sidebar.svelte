<script lang="ts">
	import { Nav } from 'sveltestrap';
</script>

<style>
	a {
		text-decoration: none;
		color: black;
		margin-left: 10px;
		font-size: 17px;
		width: 100%;
		height: 100%;
	}
	.navitem {
		padding-top: 1em;
		padding-bottom: 1em;
	}
	/*
		Pallette da modificare
	*/
	.navitem:hover {
		background-color: #c9c9c9;
	}
	.navitem:hover a {
		color: white;
	}
	a:hover {
		color: white;
	}
	#sidebar {
		z-index: 1;
		overflow-x: hidden;
		position: fixed;
		background-color: #f8f7f7;
		height: 100%;
	}
</style>

<div id="sidebar">
	<Nav vertical>
		<div class="navitem">
			<a href="report/what-is-globalization">Cos'è la globalizzazione?</a>
		</div>
		<div class="navitem">
			<a href="/">Economia</a>
		</div>
		<div class="navitem">
			<a href="/">Cultura</a>
		</div>
		<div class="navitem">
			<a href="/">Politica</a>
		</div>
	</Nav>
</div>
