const sleep = (seconds) => {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			resolve();
		}, seconds * 1000);
	});
};

async function count() {
	console.log("one");
	await sleep(1);
	console.log("two");
}

async function main() {
	const startTime = new Date().getTime();
	
	console.time("main");

	await count();
	await count();
	await count();

	console.timeEnd("main");
	
	const endTime = new Date().getTime();
	console.log(`elapsed time: ${endTime - startTime}`)
}

main();