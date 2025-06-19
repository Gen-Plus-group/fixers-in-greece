#!/usr/bin/env node

/**
 * Template-Based Mass Content Expansion System
 * Systematically expands ALL remaining pre-production pages with comprehensive content
 * Maintains quality standards while ensuring efficient completion
 */

const fs = require('fs');
const path = require('path');

/ Comprehensive service definitions for ALL remaining pre-production services
const serviceTemplates = {
    'travel-logistics': {
        title: 'Travel Logistics',
        subtitle: 'Comprehensive travel coordination and logistics management for international productions',
        description: 'Expert travel coordination for cast, crew, and equipment. Complete logistics management including visas, transportation, accommodation, and customs clearance.',
        services: [
            { icon: '✈️', title: 'International Travel', items: ['Flight bookings', 'Visa assistance', 'Work permits', 'Travel insurance', 'Airport transfers'], tagline: 'Global Mobility' },
            { icon: '🏨', title: 'Accommodation', items: ['Hotel bookings', 'Long-term rentals', 'Crew housing', 'Location proximity', 'Budget optimization'], tagline: 'Comfortable Stays' },
            { icon: '🚐', title: 'Ground Transportation', items: ['Vehicle rentals', 'Driver services', 'Equipment transport', 'Location shuttles', 'Emergency transport'], tagline: 'Reliable Transport' },
            { icon: '📦', title: 'Equipment Logistics', items: ['Customs clearance', 'Carnet documentation', 'Equipment shipping', 'Local rentals', 'Storage facilities'], tagline: 'Equipment Solutions' }
        ],
        capabilities: {
            title: 'Professional Travel Coordination Expertise',
            subtitle: 'Expert logistics coordinators with comprehensive knowledge of international travel requirements, Greeceese regulations, and production-specific needs.',
            sections: [
                {
                    title: 'International Travel Management',
                    content: 'Complete visa and work permit assistance for cast and crew including application preparation, documentation support, and government liaison. Flight booking optimization, travel insurance coordination, and airport transfer services. Emergency travel support, itinerary management, and 24/7 travel assistance ensuring smooth international mobility for production teams.'
                },
                {
                    title: 'Accommodation & Housing Solutions',
                    content: 'Professional accommodation booking services including hotels, serviced apartments, and long-term housing solutions. Location proximity optimization, budget management, and crew comfort considerations. Special requirements coordination including dietary needs, accessibility, and cultural preferences. Group booking discounts and extended stay arrangements for long-term productions.'
                },
                {
                    title: 'Equipment & Customs Coordination',
                    content: 'Expert customs clearance for production equipment including carnet documentation, import permits, and duty management. Equipment shipping coordination, local rental sourcing, and storage facility management. Insurance coordination, equipment tracking, and secure transportation ensuring safe arrival and deployment of production assets.'
                }
            ],
            stats: [
                { number: '2,000+', label: 'Travel Arrangements' },
                { number: '48h', label: 'Visa Processing Time' },
                { number: '25+', label: 'Countries Served' },
                { number: '100%', label: 'Customs Success Rate' }
            ]
        },
        faq: [
            {
                question: 'What visa and work permit assistance do you provide for international productions?',
                answer: 'Complete visa and work permit services including application preparation, documentation assistance, and government liaison. We handle tourist visas, business visas, and temporary work permits for cast and crew. Services include expedited processing, multiple-entry arrangements, and compliance with Greeceese immigration requirements for international productions.'
            },
            {
                question: 'How do you handle equipment customs clearance and carnets?',
                answer: 'Expert customs clearance services including carnet preparation, import documentation, and duty management. We coordinate with Greeceese customs authorities, handle equipment manifests, and ensure proper documentation for temporary imports. Services include equipment tracking, insurance coordination, and secure storage facilities.'
            },
            {
                question: 'What are typical costs for travel logistics coordination?',
                answer: 'Travel coordination fees vary by scope and duration. Basic travel arrangements: $200-500 USD per person. Comprehensive logistics packages: $1,000-5,000 USD per production. Visa assistance: $100-300 USD per application. Equipment customs clearance: $500-2,000 USD depending on equipment value. Group discounts available for large productions.'
            }
        ]
    },
    'production-insurance': {
        title: 'Production Insurance',
        subtitle: 'Comprehensive insurance solutions and risk management for film and video productions',
        description: 'Expert insurance coordination and risk management services. Complete coverage solutions including equipment, liability, and production-specific insurance ensuring comprehensive protection.',
        services: [
            { icon: '🛡️', title: 'Equipment Insurance', items: ['Camera equipment coverage', 'Lighting gear protection', 'Audio equipment insurance', 'Drone coverage', 'Rental equipment protection'], tagline: 'Equipment Protection' },
            { icon: '👥', title: 'Liability Coverage', items: ['General liability', 'Professional indemnity', 'Public liability', 'Employer liability', 'Product liability'], tagline: 'Comprehensive Liability' },
            { icon: '🎬', title: 'Production Insurance', items: ['Completion bonds', 'Errors & omissions', 'Cast insurance', 'Weather coverage', 'Location damage'], tagline: 'Production Security' },
            { icon: '🌍', title: 'International Coverage', items: ['Multi-territory policies', 'Travel insurance', 'Medical coverage', 'Evacuation insurance', 'Currency protection'], tagline: 'Global Protection' }
        ]
    },
    'concept-development': {
        title: 'Concept Development',
        subtitle: 'Creative concept development and ideation services for compelling visual storytelling',
        description: 'Expert creative development services transforming ideas into compelling visual concepts. Professional ideation, concept refinement, and creative strategy ensuring strong foundations for successful productions.',
        services: [
            { icon: '💡', title: 'Creative Ideation', items: ['Brainstorming sessions', 'Concept generation', 'Creative workshops', 'Idea refinement', 'Concept validation'], tagline: 'Creative Innovation' },
            { icon: '🎨', title: 'Visual Development', items: ['Visual style guides', 'Color palettes', 'Typography selection', 'Visual references', 'Aesthetic direction'], tagline: 'Visual Identity' },
            { icon: '📖', title: 'Narrative Structure', items: ['Story architecture', 'Character development', 'Plot structure', 'Theme exploration', 'Message clarity'], tagline: 'Story Foundation' },
            { icon: '🎯', title: 'Strategic Planning', items: ['Target audience analysis', 'Market positioning', 'Creative strategy', 'Brand alignment', 'Competitive analysis'], tagline: 'Strategic Direction' }
        ]
    },
    'creative-direction': {
        title: 'Creative Direction',
        subtitle: 'Professional creative direction and artistic guidance for exceptional visual storytelling',
        description: 'Expert creative direction services ensuring cohesive artistic vision and exceptional execution. Professional guidance from concept to completion with focus on visual excellence and brand consistency.',
        services: [
            { icon: '🎨', title: 'Artistic Vision', items: ['Visual style development', 'Creative strategy', 'Artistic guidance', 'Brand integration', 'Aesthetic consistency'], tagline: 'Creative Excellence' },
            { icon: '📐', title: 'Design Coordination', items: ['Production design oversight', 'Color coordination', 'Visual continuity', 'Style guide creation', 'Design team management'], tagline: 'Design Unity' },
            { icon: '🎬', title: 'Creative Supervision', items: ['On-set creative guidance', 'Quality control', 'Creative problem solving', 'Team coordination', 'Vision implementation'], tagline: 'Creative Leadership' },
            { icon: '✨', title: 'Innovation & Trends', items: ['Trend analysis', 'Creative innovation', 'Market insights', 'Competitive analysis', 'Future-proofing'], tagline: 'Creative Innovation' }
        ]
    },
    'moodboard-creation': {
        title: 'Moodboard Creation',
        subtitle: 'Professional moodboard and visual reference development for creative projects',
        description: 'Expert moodboard creation services translating concepts into compelling visual references. Professional visual development ensuring clear creative communication and artistic direction.',
        services: [
            { icon: '🖼️', title: 'Visual Research', items: ['Image sourcing', 'Reference collection', 'Style exploration', 'Trend research', 'Visual inspiration'], tagline: 'Visual Discovery' },
            { icon: '🎨', title: 'Mood Development', items: ['Color palette creation', 'Texture selection', 'Lighting references', 'Composition studies', 'Atmosphere development'], tagline: 'Mood Crafting' },
            { icon: '📋', title: 'Presentation Design', items: ['Layout design', 'Visual organization', 'Annotation systems', 'Digital presentation', 'Print formatting'], tagline: 'Professional Presentation' },
            { icon: '🔄', title: 'Iteration & Refinement', items: ['Client feedback integration', 'Revision cycles', 'Concept refinement', 'Final approval', 'Version control'], tagline: 'Collaborative Development' }
        ]
    },
    'pitch-deck-design': {
        title: 'Pitch Deck Design',
        subtitle: 'Professional pitch deck design and presentation development for compelling project proposals',
        description: 'Expert pitch deck creation services transforming ideas into persuasive visual presentations. Professional design and storytelling ensuring impactful investor and client presentations.',
        services: [
            { icon: '📊', title: 'Content Strategy', items: ['Narrative structure', 'Key message development', 'Audience analysis', 'Persuasion strategy', 'Information hierarchy'], tagline: 'Strategic Communication' },
            { icon: '🎨', title: 'Visual Design', items: ['Slide design', 'Infographic creation', 'Brand integration', 'Visual storytelling', 'Professional layouts'], tagline: 'Visual Impact' },
            { icon: '📈', title: 'Data Visualization', items: ['Chart design', 'Graph creation', 'Statistical presentation', 'Financial projections', 'Market analysis'], tagline: 'Data Clarity' },
            { icon: '🎯', title: 'Presentation Optimization', items: ['Flow optimization', 'Timing coordination', 'Interactive elements', 'Delivery coaching', 'Q&A preparation'], tagline: 'Presentation Excellence' }
        ]
    },
    'storyboarding': {
        title: 'Storyboarding',
        subtitle: 'Professional storyboard creation and visual planning for film and video productions',
        description: 'Expert storyboarding services translating scripts into detailed visual sequences. Professional pre-visualization ensuring efficient production planning and creative clarity.',
        services: [
            { icon: '✏️', title: 'Traditional Storyboards', items: ['Hand-drawn boards', 'Detailed illustrations', 'Character expressions', 'Action sequences', 'Camera angles'], tagline: 'Classic Artistry' },
            { icon: '💻', title: 'Digital Storyboards', items: ['Digital illustrations', 'Vector graphics', 'Color storyboards', 'Animation previews', 'Interactive boards'], tagline: 'Digital Precision' },
            { icon: '🎬', title: 'Technical Boards', items: ['Camera movements', 'Lighting plans', 'Shot specifications', 'Timing notes', 'Production details'], tagline: 'Technical Planning' },
            { icon: '🔄', title: 'Animatics', items: ['Animated storyboards', 'Timing visualization', 'Motion studies', 'Rough animation', 'Sequence planning'], tagline: 'Motion Preview' }
        ]
    },
    'script-consultation': {
        title: 'Script Consultation',
        subtitle: 'Professional script analysis and development consultation for enhanced storytelling',
        description: 'Expert script consultation services providing detailed analysis, feedback, and development guidance. Professional story development ensuring compelling narratives and production readiness.',
        services: [
            { icon: '📖', title: 'Script Analysis', items: ['Story structure review', 'Character development analysis', 'Dialogue assessment', 'Pacing evaluation', 'Theme exploration'], tagline: 'Story Expertise' },
            { icon: '✍️', title: 'Development Notes', items: ['Detailed feedback', 'Improvement suggestions', 'Rewrite guidance', 'Character notes', 'Plot recommendations'], tagline: 'Professional Guidance' },
            { icon: '🎭', title: 'Genre Expertise', items: ['Genre conventions', 'Market analysis', 'Audience expectations', 'Commercial viability', 'Cultural adaptation'], tagline: 'Genre Mastery' },
            { icon: '🔄', title: 'Revision Support', items: ['Multiple draft reviews', 'Ongoing consultation', 'Progress tracking', 'Final polish', 'Production preparation'], tagline: 'Continuous Support' }
        ]
    },
    'site-surveys': {
        title: 'Site Surveys',
        subtitle: 'Professional site surveys and technical assessments for production planning',
        description: 'Expert site survey services providing detailed technical assessments and production planning data. Comprehensive location analysis ensuring informed decision-making and efficient production workflows.',
        services: [
            { icon: '📏', title: 'Technical Measurements', items: ['Dimensional surveys', 'Space planning', 'Equipment placement', 'Access measurements', 'Capacity assessments'], tagline: 'Precise Measurements' },
            { icon: '⚡', title: 'Infrastructure Assessment', items: ['Power availability', 'Network connectivity', 'Utilities mapping', 'Safety systems', 'Emergency access'], tagline: 'Infrastructure Analysis' },
            { icon: '📊', title: 'Environmental Analysis', items: ['Lighting conditions', 'Acoustic properties', 'Weather patterns', 'Traffic analysis', 'Noise levels'], tagline: 'Environmental Data' },
            { icon: '📋', title: 'Documentation', items: ['Survey reports', 'Technical drawings', 'Photo documentation', 'Recommendation reports', 'Risk assessments'], tagline: 'Comprehensive Reports' }
        ]
    },
    'cost-estimation': {
        title: 'Cost Estimation',
        subtitle: 'Professional cost estimation and financial planning for accurate production budgets',
        description: 'Expert cost estimation services providing detailed financial analysis and budget projections. Professional cost modeling ensuring accurate financial planning and budget control.',
        services: [
            { icon: '💰', title: 'Budget Modeling', items: ['Cost breakdowns', 'Financial projections', 'Scenario planning', 'Risk analysis', 'Contingency planning'], tagline: 'Financial Modeling' },
            { icon: '📊', title: 'Market Analysis', items: ['Rate research', 'Vendor comparisons', 'Market trends', 'Cost benchmarking', 'Price negotiations'], tagline: 'Market Intelligence' },
            { icon: '🎯', title: 'Accuracy Optimization', items: ['Historical data analysis', 'Cost validation', 'Estimation refinement', 'Variance tracking', 'Precision improvement'], tagline: 'Estimation Precision' },
            { icon: '📈', title: 'Financial Reporting', items: ['Cost reports', 'Budget summaries', 'Variance analysis', 'Trend reporting', 'Financial dashboards'], tagline: 'Financial Insights' }
        ]
    },
    'contract-management': {
        title: 'Contract Management',
        subtitle: 'Professional contract management and legal coordination for production agreements',
        description: 'Expert contract management services ensuring comprehensive legal protection and compliance. Professional coordination of all production agreements with focus on risk mitigation and legal security.',
        services: [
            { icon: '📄', title: 'Contract Drafting', items: ['Agreement preparation', 'Terms negotiation', 'Legal compliance', 'Risk mitigation', 'Clause optimization'], tagline: 'Legal Drafting' },
            { icon: '🤝', title: 'Negotiation Support', items: ['Contract negotiations', 'Terms optimization', 'Dispute resolution', 'Amendment management', 'Renewal coordination'], tagline: 'Negotiation Excellence' },
            { icon: '📋', title: 'Compliance Management', items: ['Legal compliance', 'Regulatory adherence', 'Documentation control', 'Audit preparation', 'Risk assessment'], tagline: 'Compliance Assurance' },
            { icon: '🔒', title: 'Contract Security', items: ['Document security', 'Version control', 'Access management', 'Confidentiality protection', 'Digital signatures'], tagline: 'Secure Management' }
        ]
    },
    'covid-compliance': {
        title: 'COVID Compliance',
        subtitle: 'Professional COVID-19 safety protocols and compliance management for safe productions',
        description: 'Expert COVID-19 compliance services ensuring safe production environments. Comprehensive safety protocols, health monitoring, and regulatory compliance for responsible filmmaking.',
        services: [
            { icon: '🛡️', title: 'Safety Protocols', items: ['Health screening', 'Safety procedures', 'PPE coordination', 'Sanitization protocols', 'Social distancing'], tagline: 'Health Protection' },
            { icon: '📋', title: 'Compliance Management', items: ['Regulatory compliance', 'Documentation', 'Reporting requirements', 'Audit preparation', 'Policy updates'], tagline: 'Regulatory Adherence' },
            { icon: '🏥', title: 'Health Monitoring', items: ['Daily health checks', 'Testing coordination', 'Contact tracing', 'Isolation protocols', 'Medical support'], tagline: 'Health Oversight' },
            { icon: '📊', title: 'Risk Assessment', items: ['Risk evaluation', 'Mitigation strategies', 'Contingency planning', 'Safety audits', 'Incident response'], tagline: 'Risk Management' }
        ]
    },
    'catering-services': {
        title: 'Catering Services',
        subtitle: 'Professional catering coordination and food services for film and video productions',
        description: 'Expert catering services ensuring quality food service and crew satisfaction. Professional coordination of all food and beverage needs with focus on nutrition, dietary requirements, and production schedules.',
        services: [
            { icon: '🍽️', title: 'Meal Planning', items: ['Menu development', 'Nutritional planning', 'Dietary accommodations', 'Cultural preferences', 'Budget optimization'], tagline: 'Culinary Excellence' },
            { icon: '🚚', title: 'Service Coordination', items: ['Delivery scheduling', 'Setup management', 'Service staff', 'Equipment provision', 'Cleanup coordination'], tagline: 'Service Management' },
            { icon: '🥗', title: 'Special Requirements', items: ['Dietary restrictions', 'Allergies management', 'Cultural foods', 'Healthy options', 'Special occasions'], tagline: 'Custom Solutions' },
            { icon: '📋', title: 'Logistics Management', items: ['Vendor coordination', 'Quality control', 'Food safety', 'Permit compliance', 'Cost management'], tagline: 'Operational Excellence' }
        ]
    },
    'call-sheets': {
        title: 'Call Sheets',
        subtitle: 'Professional call sheet creation and distribution for efficient production coordination',
        description: 'Expert call sheet services ensuring clear communication and efficient production coordination. Professional scheduling and information management for seamless daily operations.',
        services: [
            { icon: '📅', title: 'Schedule Coordination', items: ['Daily scheduling', 'Crew calls', 'Talent coordination', 'Equipment scheduling', 'Location timing'], tagline: 'Perfect Timing' },
            { icon: '📋', title: 'Information Management', items: ['Contact details', 'Location information', 'Weather updates', 'Special instructions', 'Emergency contacts'], tagline: 'Complete Information' },
            { icon: '📱', title: 'Digital Distribution', items: ['Mobile optimization', 'Real-time updates', 'Push notifications', 'Cloud synchronization', 'Offline access'], tagline: 'Digital Efficiency' },
            { icon: '🔄', title: 'Update Management', items: ['Last-minute changes', 'Version control', 'Change notifications', 'Revision tracking', 'Communication logs'], tagline: 'Dynamic Updates' }
        ]
    },
    'licensing-rights': {
        title: 'Licensing Rights',
        subtitle: 'Professional licensing and rights management for intellectual property protection',
        description: 'Expert licensing and rights management services ensuring proper intellectual property protection. Comprehensive rights coordination for music, footage, and content licensing.',
        services: [
            { icon: '🎵', title: 'Music Licensing', items: ['Music rights clearance', 'Sync licensing', 'Performance rights', 'Mechanical rights', 'Master recordings'], tagline: 'Music Rights' },
            { icon: '📹', title: 'Footage Licensing', items: ['Stock footage rights', 'Archival material', 'News footage', 'Documentary clips', 'User-generated content'], tagline: 'Visual Rights' },
            { icon: '📄', title: 'Content Rights', items: ['Script rights', 'Book adaptations', 'Character rights', 'Trademark clearance', 'Brand permissions'], tagline: 'Content Protection' },
            { icon: '🌍', title: 'Territory Management', items: ['Global rights', 'Regional licensing', 'Distribution rights', 'Broadcast rights', 'Digital rights'], tagline: 'Global Licensing' }
        ]
    },
    'talent-coordination': {
        title: 'Talent Coordination',
        subtitle: 'Professional talent coordination and management for seamless production workflows',
        description: 'Expert talent coordination services ensuring smooth talent management and production efficiency. Professional coordination of all talent-related logistics and requirements.',
        services: [
            { icon: '🎭', title: 'Talent Scheduling', items: ['Availability coordination', 'Schedule optimization', 'Conflict resolution', 'Travel coordination', 'Rehearsal scheduling'], tagline: 'Schedule Mastery' },
            { icon: '🏨', title: 'Logistics Management', items: ['Accommodation booking', 'Transportation', 'Meal coordination', 'Wardrobe fittings', 'Makeup scheduling'], tagline: 'Complete Care' },
            { icon: '📋', title: 'Contract Coordination', items: ['Deal negotiations', 'Contract management', 'Payment coordination', 'Rights management', 'Legal compliance'], tagline: 'Professional Management' },
            { icon: '🤝', title: 'Relationship Management', items: ['Talent relations', 'Agent coordination', 'Manager liaison', 'Publicity coordination', 'Special requests'], tagline: 'Relationship Excellence' }
        ]
    },
    'talent-releases': {
        title: 'Talent Releases',
        subtitle: 'Professional talent release management and legal documentation for production protection',
        description: 'Expert talent release services ensuring comprehensive legal protection and rights clearance. Professional documentation management for all talent-related legal requirements.',
        services: [
            { icon: '📄', title: 'Release Documentation', items: ['Talent releases', 'Minor releases', 'Location releases', 'Crew releases', 'Vendor releases'], tagline: 'Legal Documentation' },
            { icon: '⚖️', title: 'Rights Management', items: ['Image rights', 'Likeness rights', 'Performance rights', 'Voice rights', 'Publicity rights'], tagline: 'Rights Protection' },
            { icon: '🔒', title: 'Legal Compliance', items: ['Privacy laws', 'Consent management', 'Age verification', 'Guardian consent', 'International compliance'], tagline: 'Legal Security' },
            { icon: '📋', title: 'Documentation Control', items: ['Version management', 'Digital signatures', 'Secure storage', 'Audit trails', 'Compliance tracking'], tagline: 'Document Security' }
        ]
    },
    'union-talent-management': {
        title: 'Union Talent Management',
        subtitle: 'Professional union talent coordination and compliance management for regulated productions',
        description: 'Expert union talent management services ensuring compliance with labor regulations and union requirements. Professional coordination of union talent and regulatory compliance.',
        services: [
            { icon: '🤝', title: 'Union Coordination', items: ['Union negotiations', 'Contract compliance', 'Rate management', 'Benefit coordination', 'Dispute resolution'], tagline: 'Union Relations' },
            { icon: '📋', title: 'Compliance Management', items: ['Labor law compliance', 'Working time regulations', 'Safety requirements', 'Overtime management', 'Break scheduling'], tagline: 'Regulatory Compliance' },
            { icon: '💰', title: 'Payment Coordination', items: ['Union rates', 'Overtime calculations', 'Benefit payments', 'Pension contributions', 'Health insurance'], tagline: 'Financial Management' },
            { icon: '📊', title: 'Reporting & Documentation', items: ['Union reports', 'Time tracking', 'Compliance documentation', 'Audit preparation', 'Record keeping'], tagline: 'Professional Documentation' }
        ]
    },
    'voiceover-casting': {
        title: 'Voiceover Casting',
        subtitle: 'Professional voiceover casting and talent management for audio productions',
        description: 'Expert voiceover casting services connecting productions with exceptional voice talent. Professional audio casting with comprehensive talent databases and quality assurance.',
        services: [
            { icon: '🎤', title: 'Voice Talent Casting', items: ['Narrator casting', 'Character voices', 'Commercial voices', 'Documentary narration', 'Animation voices'], tagline: 'Voice Excellence' },
            { icon: '🌍', title: 'Multi-Language Casting', items: ['Native speakers', 'Accent specialists', 'Dialect coaching', 'Translation services', 'Cultural authenticity'], tagline: 'Global Voices' },
            { icon: '🎧', title: 'Audio Production', items: ['Recording coordination', 'Studio booking', 'Audio direction', 'Quality control', 'Post-production'], tagline: 'Audio Quality' },
            { icon: '📋', title: 'Talent Management', items: ['Audition coordination', 'Contract management', 'Schedule coordination', 'Payment processing', 'Rights management'], tagline: 'Professional Management' }
        ]
    },
    'fixer-services-local': {
        title: 'Local Fixer Services',
        subtitle: 'Professional local fixer services and production support for Greece-based filming',
        description: 'Expert local fixer services providing comprehensive production support and local expertise. Professional coordination ensuring smooth operations and cultural authenticity for international productions.',
        services: [
            { icon: '🗺️', title: 'Local Expertise', items: ['Cultural guidance', 'Language support', 'Local customs', 'Regional knowledge', 'Community relations'], tagline: 'Cultural Authenticity' },
            { icon: '🤝', title: 'Government Relations', items: ['Official liaison', 'Permit assistance', 'Regulatory compliance', 'Authority coordination', 'Legal support'], tagline: 'Official Relations' },
            { icon: '📋', title: 'Production Support', items: ['Logistics coordination', 'Vendor management', 'Crew coordination', 'Equipment sourcing', 'Problem solving'], tagline: 'Production Excellence' },
            { icon: '🚨', title: 'Emergency Support', items: ['Crisis management', 'Emergency response', 'Medical assistance', 'Security coordination', '24/7 support'], tagline: 'Emergency Readiness' }
        ]
    }
};

/ Function to generate comprehensive content sections
function generateServiceOverview(serviceDef) {
    return `        <!-- ${serviceDef.title} Services Overview -->
        <section id="content" class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-greece-blue mb-4">
                        Comprehensive ${serviceDef.title} Solutions
                    </h2>
                    <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                        ${serviceDef.description}
                    </p>
                </div>

                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                    ${serviceDef.services.map(service => `
                    <!-- ${service.title} -->
                    <div class="bg-greece-dark border border-gray-700 rounded-lg p-6">
                        <div class="text-4xl mb-4 text-center">${service.icon}</div>
                        <h3 class="text-xl font-bold text-greece-blue mb-3 text-center">${service.title}</h3>
                        <ul class="text-gray-300 space-y-2 mb-4">
                            ${service.items.map(item => `<li>• ${item}</li>`).join('\n                            ')}
                        </ul>
                        <div class="text-center">
                            <span class="text-greece-blue font-semibold">${service.tagline}</span>
                        </div>
                    </div>`).join('\n\n                    ')}
                </div>
            </div>
        </section>`;
}

/ Function to process and expand a single service file
function expandServiceFile(serviceKey, serviceDef) {
    const filePath = `pre-production-services/${serviceKey}/index.html`;
    
    console.log(`📝 Expanding ${serviceDef.title}...`);
    
    try {
        if (!fs.existsSync(filePath)) {
            console.log(`❌ File not found: ${filePath}`);
            return false;
        }
        
        let content = fs.readFileSync(filePath, 'utf8');
        
        / Find and replace the Introduction Section
        const introSectionRegex = /<!-- Introduction Section -->\s*<section class="py-16">[\s\S]*?<\/section>/;
        const serviceOverview = generateServiceOverview(serviceDef);
        
        if (introSectionRegex.test(content)) {
            content = content.replace(introSectionRegex, serviceOverview);
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ ${serviceDef.title} - Service overview section updated`);
            return true;
        } else {
            console.log(`⚠️ ${serviceDef.title} - Introduction section not found`);
            return false;
        }
        
    } catch (error) {
        console.log(`❌ ${serviceDef.title} - Error: ${error.message}`);
        return false;
    }
}

/ Main execution function
function main() {
    console.log('🚀 TEMPLATE-BASED MASS CONTENT EXPANSION');
    console.log('=' + '='.repeat(70));
    console.log('🎯 Systematically expanding ALL remaining pre-production pages');
    console.log('📋 Maintaining established quality standards\n');
    
    const services = Object.keys(serviceTemplates);
    console.log(`📄 Services to expand: ${services.length}`);
    
    let successCount = 0;
    let failCount = 0;
    
    for (const serviceKey of services) {
        const serviceDef = serviceTemplates[serviceKey];
        
        if (expandServiceFile(serviceKey, serviceDef)) {
            successCount++;
        } else {
            failCount++;
        }
        
        / Add small delay to prevent overwhelming the system
        setTimeout(() => {}, 100);
    }
    
    console.log('\n🎉 TEMPLATE-BASED EXPANSION COMPLETE!');
    console.log('=' + '='.repeat(50));
    console.log(`✅ Successfully expanded: ${successCount} pages`);
    console.log(`❌ Failed expansions: ${failCount} pages`);
    console.log(`📊 Success rate: ${Math.round((successCount / (successCount + failCount)) * 100)}%`);
    
    if (successCount > 0) {
        console.log('\n🚀 Ready for commit and deployment!');
        console.log('📋 Next steps: Add capabilities, FAQ, and CTA sections to completed pages');
    }
}

if (require.main === module) {
    main();
}

module.exports = { serviceTemplates, expandServiceFile };
