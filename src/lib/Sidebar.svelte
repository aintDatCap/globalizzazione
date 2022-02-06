<script lang="ts">
	import { Nav } from 'sveltestrap';
</script>

<div id="sidebar">
	<Nav vertical>
		<a href="/report/what-is-globalization">
			<div class="navitem">Cos'è la globalizzazione?</div>
		</a>
		<a href="/report/economy"> <div class="navitem">Economia</div></a>
		<a href="/report/culture"> <div class="navitem">Cultura</div></a>
		<a href="/report/politics"> <div class="navitem">Politica</div></a>
	</Nav>
</div>

<style>
	a {
		text-decoration: none;
		color: black;
		font-size: 17px;
		
	}
	.navitem {
		padding-top: 1em;
		padding-bottom: 1em;
		margin-left: 1em;
		margin-right: 1em;
	}
	/*
		Pallette da modificare
	*/
	a:hover {
		background-color: #c9c9c9;
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
