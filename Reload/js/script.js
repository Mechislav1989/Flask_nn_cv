window.addEventListener('DOMContentLoaded', () => {

    const tabs =  document.querySelectorAll('.contacts') 
        tabsContent = document.querySelectorAll('.contanct_link')  
        tabsParent = document.querySelectorAll('.contact_type')

    function hideTabContent() {
        tabsContent.forEach(item =>{
            item.style.display = 'none';
        })
        tabs.forEach(item =>{
            item.classList.remove('.tech_skills_item');
        });
    }

    function showTabContant(i) {
        tabsContent[i].style.display = 'block';
        item.classList.add('.tech_skills_item');
    }

    hideTabContent();
    showTabsContent();
});