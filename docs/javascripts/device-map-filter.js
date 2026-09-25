// Static links and preview pages remain usable without JavaScript.
function initializeMapFilter() {
  const list = document.getElementById('deviceMapList');
  if (!list || list.dataset.filterReady) return;
  list.dataset.filterReady = 'true';
  const search = document.getElementById('mapSearch');
  const manufacturer = document.getElementById('manufacturerFilter');
  const count = document.getElementById('mapCount');
  const rows = Array.from(list.children);
  function filter() {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    rows.forEach(row => {
      row.hidden = !row.dataset.search.toLocaleLowerCase().includes(query) ||
        (manufacturer.value !== '' && row.dataset.manufacturer !== manufacturer.value);
      if (!row.hidden) visible++;
    });
    count.textContent = `${visible} of ${rows.length} public previews`;
  }
  search.addEventListener('input', filter);
  manufacturer.addEventListener('change', filter);
  document.querySelector('.map-filters').hidden = false;
  filter();
}
if (typeof document$ !== 'undefined') document$.subscribe(initializeMapFilter);
else if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initializeMapFilter);
else initializeMapFilter();
