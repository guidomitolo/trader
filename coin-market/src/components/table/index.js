import React, { useState, useEffect } from 'react';
import cacheHistoryRequest from '../cache.js'
import { get_db } from '../async.js';


const TablePage = function() {
    const [coins, setCoins] = useState([])
    const [selectedCoin, setSelectedCoin] = useState(null)

    useEffect(() => {
        get_db("/api/coin/").then(dbData => {
            setCoins(dbData.results);
        })
    }, []);

    if (!coins) {
        return <div>No coins</div>
    }

    return(
        <div class="mt-2">
            <select onChange={(e) => setSelectedCoin(e.target.value)}>
                <option>Select Coin</option>
                {
                    coins.map((coin, index) => {
                        return (
                            <option key={index} value={coin.code}>{coin.name}</option>
                        );
                    })
                }
            </select>
            <TableData
                page="1"
                coin={selectedCoin}
            />
        </div>
    )
}

const TableData = function ({page, coin}) {

    if (coin) {
        const [data, isLoading, currentPage, getData] = cacheHistoryRequest(
            `/api/history/${coin}/?page=${page}`,
            []
        )
    
        if(isLoading) {
            return <div>Loading</div>
        }
    
        if((!data.count || data.count === 0)){
            return <div>No Records</div>
        }
            
        return(
            <div>
                <div>
                <RenderTable 
                    records={data.results}
                    total={data.count}
                />
                </div>
                <div>
                    <button class="btn btn-secondary m-2" type='button' onClick={ () => getData(`/api/history/${coin}/?page=${currentPage - 1}`)}>Previous</button>
                    {currentPage}
                    <button class="btn btn-secondary m-2" type='button' onClick={ () => getData(`/api/history/${coin}/?page=${currentPage + 1}`)}>Next</button>
                </div>
            </div>
        )
    }

    return <div>No selection</div>

}

const RenderTable = function ({records, total}) {

    const datetimeOptions = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' }

    return (
        <table class="table table-sm">
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Pirce</th>
                    <th>Market Cap</th>
                    <th>Total Volume</th>
                </tr>
            </thead>
            <tbody>
                {
                    records.map((item, index) => {
                        return (
                            <tr key={index}>
                                <td>
                                    {
                                        new Intl.DateTimeFormat('en-US', datetimeOptions).format(new Date(item.timestamp))
                                    }
                                </td>
                                <td>
                                    {
                                        item.currency + " " + item.price
                                    }
                                </td>
                                <td>
                                    {
                                        item.market_cap
                                    }
                                </td>
                                <td>
                                    {
                                        item.total_volume
                                    }
                                </td>
                            </tr>
                        );
                    })
                }
            </tbody>
        </table>
    )
}

export default TablePage;