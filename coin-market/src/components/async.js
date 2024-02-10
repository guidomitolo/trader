const get_db = async function async_query(url) {

    return await fetch(url)
    .then(res => res.json())
    .then((data) => data)
    .catch((error) => {
        console.log('failed', error)
        return []
    });
};


export { get_db }