<script lang="ts">
	import Navbar from '$lib/navbar.svelte';
	import globImg from '$lib/assets/index/globalization.png';
	import econImg from '$lib/assets/index/economy.png';
	import cultImg from '$lib/assets/index/culture.png';
	import migrImg from '$lib/assets/index/migration.png';
	import techImg from '$lib/assets/index/technology.png';
	import envImg from '$lib/assets/index/enviroment.png';
	import covImg from '$lib/assets/index/covid.png';
	import { Carousel, CarouselControl, CarouselIndicators, CarouselItem } from 'sveltestrap';

	let activeIndex = 0;
	const images = [globImg, econImg, cultImg, migrImg, techImg, envImg, covImg];
	const links = [
		'what-is-globalization',
		'economy',
		'culture',
		'migration',
		'technology',
		'enviroment',
		'covid'
	];
	for (let i = 0; i < links.length; i++) {
		links[i] = '/report/' + links[i];
	}
	/*	setInterval(() => {
		if (activeIndex == images.length - 1) activeIndex = 0;
		else activeIndex++;
	}, 10000);*/
</script>

<style>
	.disclamer {
		text-align: center;
	}
	#quick_description {
		text-align: center;
		font-size: 20px;
	}
	#carousel {
		width: 600px;
		height: 600px;
		margin: auto;
	}
	img {
		margin: auto;
	}
</style>

<Navbar />

<p class="disclamer">By Giovanni Sandri e Federico Caprini</p>

<p id="quick_description">
	<!--sostenitaly.it-->
	Sito ufficiale del rapporto dei rappresentanti della sostenibilità ambientale dello Stato italiano
	sulla globalizzazione.
</p>

<a href={links[activeIndex]}>
	<div id="carousel">
		<Carousel dark items={images} bind:activeIndex>
			
			<CarouselIndicators bind:activeIndex items={images} />

			<div class="carousel-inner">
				{#each images as item, index}
					<CarouselItem bind:activeIndex itemIndex={index}>
						<img src={item} width="400px" height="400px"class="d-block" alt={`${item} ${index + 1}`} />
					</CarouselItem>
				{/each}
			</div>
			<CarouselControl direction="prev" bind:activeIndex items={images} />
			<CarouselControl direction="next" bind:activeIndex items={images} />
		</Carousel>
	</div>
</a>
