<script>
	import Navbar from '$lib/navbar.svelte';
	import globalizationImg from '$lib/assets/globalization.png';
</script>

<Navbar />

<article>
	<h2 class="title">Cos'è la globalizzazione?</h2>
	<div>
		<p class="description">
			Il termine globalizzazione è un termine che è stato adoperato dagli anni `80 in poi per
			indicare un ampio insieme di fenomeni che hanno portato ad un avvicinamento delle culture ma
			la sua origine è più antica e alcuni studiosi pensano che derivi da un ossimoro utilizzato
			negli anni `60 dal sociologo canadese McLuhan.
		</p>
		<img src={globalizationImg} alt="Globalization" height="300px" width="300px" />
	</div>
</article>

<style>
	.description {
		margin-left: 3em;
		text-align: justify;
	}

	.title {
		margin-left: 1em;
	}
	img {
    float:left;
  }

</style>
