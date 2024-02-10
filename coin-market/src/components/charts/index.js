import React, { useState, useEffect } from 'react';
import CoinChart from './chart';
import { get_db } from '../async';


const ChartsPage = function() {
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
      <div>
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
          <CoinChart 
            coin={selectedCoin}
            const days="3"
          />
      </div>
  )
}

export default ChartsPage;