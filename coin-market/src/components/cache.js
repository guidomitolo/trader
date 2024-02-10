import { useState, useEffect } from 'react';
import { get_db } from './async';

const CACHE = {}


export default function cacheHistoryRequest(url) {
    const [frontData, setFrontData] = useState([]);
    const [isLoading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);

    useEffect(() => {
        getData(url)
    }, [url]);

    const getData = (url) => {
        if (CACHE[url] !== undefined) {
            setFrontData(CACHE[url]);
            setLoading(false);
        } else {
            setLoading(true);
        }

        get_db(url).then(dbData => {
            CACHE[url] = dbData;
            setFrontData(dbData);
            setLoading(false);

            let next_page = !dbData.next || dbData.next == null ? null : new URLSearchParams(new URL(dbData.next).search).get("page")
            if (next_page) {
                setCurrentPage(next_page - 1)
            } else {
                let previous_page =  !dbData.previous || dbData.previous == null ? null : new URLSearchParams(new URL(dbData.previous).search).get("page")
                if (previous_page) {
                    setCurrentPage(previous_page + 1)
                }
            }
        });
    }

    return [frontData, isLoading, currentPage, getData];
}